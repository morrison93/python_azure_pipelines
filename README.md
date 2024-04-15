# Goals and objectives 

The goal of this project is to build a python package and then publish it on an Azure Artifact Feed in the Azure Devops ecosystem.  
The build phase is done throught setuptools to generate a ```.whl``` package.  
After that we use Twine for authentification and uploading it on an Azure Artifact Feed.

# Requirements

For this app to be working you'll have to create an artifact feed via the Azure Artifact Interface.  
Then you'll have to create a file called ```.pypirc``` where you put the code give by Azure when you click on connect to the feed.

# How was that about

We created a python project using flask framework. We created a pipeline to automate the build and publish tasks. The pipeline is generic to allows it to be modular and reused.  
You can use the tasks and personnalize the pipeline to make it fits your needs.