# CLI-CNCF-Landscape
CLI-CNCF-Landscape is a command-line tool that provides a convenient way to interact with the Cloud Native Computing Foundation (CNCF) Landscape API. The CNCF Landscape is a collection of open-source projects in the cloud native ecosystem, ranging from container orchestration and networking to storage and monitoring.

This CLI tool allows users to retrieve information about various projects, categories, and other details present in the CNCF Landscape. It simplifies the process of accessing and exploring the rich ecosystem of cloud native tools and projects that the CNCF supports.

# Features
- Project Information: Easily fetch details about specific projects in the CNCF Landscape, including their names, descriptions, and links.

- Category Listings: Retrieve a list of categories within the CNCF Landscape, helping you explore projects based on their functionality and purpose.

- Filtering: Filter projects and categories based on different criteria, such as project status, maturity level, and more.

- Search: Search for projects by name or keyword, making it efficient to find projects related to specific technologies or concepts.

# Installation
You can install CLI-CNCF-Landscape using the following methods:

**From Source**
- Clone the repository:
```git clone https://github.com/satyampsoni/CLI-CNCF-Landscape.git
```
**Navigate to the repository directory:**
```
cd CLI-CNCF-Landscape
```
**Install the tool:**
```
python setup.py install
```

**Usage**
The CLI-CNCF-Landscape tool provides a set of commands to interact with the CNCF Landscape API. Here are some example commands:

- Fetch Project Information
  To fetch information about a specific project:
```
cli-cncf-landscape project <project-name>
Replace <project-name> with the name of the project you want to retrieve information about.
```
 - List Categories
   To list all available categories within the CNCF Landscape:
   ```
    cli-cncf-landscape categories
   ```
- Filter Projects
  To filter projects based on specific criteria:
  ```
cli-cncf-landscape filter --status <status> --maturity <maturity>
Replace <status> with the desired project status (e.g., "graduated", "incubating") and <maturity> with the desired maturity level (e.g., "sandbox", "graduated").
```

- Search Projects
To search for projects by name or keyword:
```
cli-cncf-landscape search <search-query>
Replace <search-query> with the keyword you want to search for.
```
