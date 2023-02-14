# Basic stuff
import re
import click
from os import environ
from pathlib import Path
from datetime import datetime

# Jupyter stuff
import nbformat
from nbclient import NotebookClient

# Github stuff
from github import Github
GITHUB_ACTIONS = environ.get("GITHUB_ACTIONS")
GITHUB_REF = environ.get("GITHUB_REF")
GITHUB_SHA = environ.get("GITHUB_SHA")
GITHUB_TEMPLATE = """
The script in `{notebook_name}` has failed.

Here is what went wrong:
```python
{exception}
```

A branch has been created automatically at `{head_branch}`. Please push your fixes there and when it's fixed alert the Slack channel.
"""
if GITHUB_ACTIONS:
    # If we're live, connect to the GitHub API
    GITHUB_TOKEN = environ.get("GITHUB_TOKEN")
    GITHUB_CLIENT = Github(GITHUB_TOKEN)
    GITHUB_REPO = GITHUB_CLIENT.get_repo("datadesk/california-coronavirus-scrapers")

# Paths
NOTEBOOK_DIR = Path(__file__).parent.absolute()


def _strip_color(s):
    """
    Removes any color from the provided Python exception string.
    """
    return re.sub("\x1b\\[(K|.*?m)", "", s)


def _handle_exception(slug, exception):
    """
    Let the world know something has gone wrong.
    """
    # Print out to the shell
    notebook_name = f"{slug}.ipynb"
    notebook_path = NOTEBOOK_DIR.joinpath(notebook_name)
    click.echo(f'Error executing {notebook_path}', err=True)
    click.echo(exception, err=True)

    # If we're inside Github rn ...
    if GITHUB_ACTIONS:
        # Put together everything we need for pull request
        title = f"Fix for {slug.replace('-', ' ').title()} County places scraper"
        timestamp = datetime.now().timestamp()
        head_branch = f"fix-{notebook_path.stem}-{timestamp}"
        body = GITHUB_TEMPLATE.format(
            notebook_name=notebook_name,
            exception=_strip_color(str(exception)),
            head_branch=head_branch,
        ).strip()
        relative_path = f"places/{notebook_name}"

        # Open up the errored out output notebook
        output_path = NOTEBOOK_DIR.joinpath(f"{slug}-output.ipynb")
        with open(output_path, "r") as f:
            # Create a branch on github
            GITHUB_REPO.create_git_ref(ref=f"refs/heads/{head_branch}", sha=GITHUB_SHA)

            # Get the current SHA of the errored file
            sha = GITHUB_REPO.get_contents(path=relative_path, ref=GITHUB_REF).sha

            # Commit it to the new branch
            GITHUB_REPO.update_file(
                path=relative_path,
                message="Failed run of notebook",
                content=f.read(),
                sha=sha,
                branch=head_branch,
            )

            # Send up a pull request to github
            return GITHUB_REPO.create_pull(
                title=title,
                body=body,
                base=GITHUB_REF,
                head=head_branch,
                draft=True
            )


@click.command()
def main():
    slug_list = [
        'alameda',
        #'amador', #no map but collecting data
        # 'butte',
        'calaveras',
        'contra-costa',
        # 'el-dorado',
        'fresno', #no map but collecting data
        'humboldt',
        'imperial',
        #'kern',
        'kings',
        'lake',
        'long-beach',
        'los-angeles',
        'madera',
        'marin',
        'mendocino',
        'merced',
        'mono',
        'monterey',
        'napa',
        'nevada',
        'orange',
        'pasadena',
        #'placer',
        # 'plumas',
        'riverside',
        'sacramento',
        'san-bernardino',
        'san-diego',
        'san-francisco',
        'san-joaquin',
        'san-luis-obispo',
        'san-mateo',
        'santa-barbara',
        'santa-clara',
        'santa-cruz',
        'shasta',
        #'sierra',
        'siskiyou',
        'solano',
        'sonoma',
        #'stanislaus',
        # 'sutter',
        'trinity',
        'tulare',
        'ventura',
        'yolo',
        'yuba',
    ]
    print(f"Scraping {len(slug_list)} agency place lists")

    # Loop through them ...
    exceptions = []
    for slug in slug_list:
        try:
            # Run the notebooks
            input_path = NOTEBOOK_DIR.joinpath(f"{slug}.ipynb")
            click.echo(f"🐍🗒️ Running {input_path}")
            with open(input_path) as f:
                nb = nbformat.read(f, as_version=4)
            client = NotebookClient(
                nb,
                timeout=600,
                kernel_name='python3',
                allow_errors=False,
                force_raise_errors=True,
                resources={'metadata': {'path': NOTEBOOK_DIR}}
            )
            client.execute()
        except Exception as e:
            # If there's an error, stuff 'em here.
            exceptions.append([slug, e])
        finally:
            output_path = NOTEBOOK_DIR.joinpath(f"{slug}-output.ipynb")
            with open(output_path, mode="w", encoding="utf-8") as f:
                nbformat.write(nb, f)

    # If we've got exceptions, spread the word.
    if exceptions:
        [_handle_exception(slug, exception) for slug, exception in exceptions]


if __name__ == "__main__":
    main()
