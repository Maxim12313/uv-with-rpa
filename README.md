# Notes 1
- Turns out the conda.yaml file is optional. Just delete it from config and it won't try to rebuild envrionment on its own
- Can more efficiently setup the environment by using uv, avoiding minimamba install and pip 
- minimamba was the major time killer
- To make robocorp use uv, we define in robot.yaml our task shell execution as 'uv run robocorp.tasks run \<task_file_name\>'
- Flow: define uv.lock, build envrionment, source environment, change robot.yaml, run the robot

# Notes 2
- For local development and interacting with control room, we need to designate environment variables:
```
RC_WORKITEM_ADAPTER="FileAdapter"
RC_WORKITEM_INPUT_PATH="wherever"
RC_WORKITEM_OUTPUT_PATH="wherever"
```
- We can load this from a .env file or with os module
