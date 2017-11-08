# Robin Powered Presence Function

Lambda function that receives a Density API webhook and posts to a Robin Powered space to update its presence.

Robin Powered's presence module relies upon a unique user being in the space. Because our device is anonymous, we won't know the "User" who is present in the space. Therefore, you need to create a "Density Presence Bot" user and utilize that user_id for indicating presence. 

## Requirements

- Density Presence Bot user account on Robin Powered API (https://docs.robinpowered.com/docs/add-new-user-to-organization)
- AWS CLI (https://aws.amazon.com/cli/)
- Setup AWS components via: 
  - Lambda with Env vars
  - API Gateway

## Manual Setup

- Create Density Presence Bot on Robin Powered API
- Login to AWS
- Create Lambda function "Author from scratch"
- Choose an existing Role - `lambda_basic_execution` IAM role
- Create function
- Change runtime to Python 2.7 and save
- Scroll down to Environment Variables section and add in Environment Variables (noted in Env vars section below)
- Save
- Click Triggers
- Add Trigger
- Click the box and select API Gateway
- Click "Enter Value" to clear out previous API names if they exist, and name it whatever you'd like
- Click "Enter Value" to clear out previous Deployment stage if exists, and name it prod
- Change Security to "Open"
- Click Submit
- Open up "details" and copy Invoke URL
- Head to https://dashboard.density.io/#/dev/webhooks and add a new webhook with that Invocation URL
- Run `./deploy.sh` below and follow the directions to deploy Lambda function

You're all done! When people enter the space you specified in the Env vars, you'll see the presence of the Density Presence Bot.


### Lambda Env Vars

| Env Variable | Description |
| ------------- | ------------- |
| `ROBIN_USER_ID` | The Density Presence Bot user_id that "appears" in the space when it is occupied |
| `ROBIN_SPACE_ID` | The ID of the Robin space to update for presence |
| `ROBIN_API_TOKEN` | Robin Access Token to use for API requests |
| `DENSITY_SPACE_ID` | The ID of the Density space you want to correlate with the Robin space |

## Deployment

- `./deploy.sh` to deploy.