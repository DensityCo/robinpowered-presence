# Robin Powered Presence Function

Lambda function that receives a Density API webhook and posts to a Robin Powered space to update its presence.

Robin Powered's presence module relies upon a unique user being in the space. Because our device is anonymous, we won't know the "User" who is present in the space. Therefore, you need to create a "Density Presence Bot" user and utilize that user_id for indicating presence. 

## Requirements

- Density Presence Bot user account on Robin Powered API (https://docs.robinpowered.com/docs/add-new-user-to-organization)
- AWS CLI (https://aws.amazon.com/cli/)
- Setup AWS components via: 
  - Lambda with Env vars
  - API Gateway

### Lambda Env Vars

| Env Variable | Description |
| ------------- | ------------- |
| `ROBIN_USER_ID` | The Density Presence Bot user_id that "appears" in the space when it is occupied |
| `ROBIN_SPACE_ID` | The ID of the Robin space to update for presence |
| `ROBIN_API_TOKEN` | Robin Access Token to use for API requests |
| `DENSITY_SPACE_ID` | The ID of the Density space you want to correlate with the Robin space |

## Deployment

- `./deploy.sh` to deploy.