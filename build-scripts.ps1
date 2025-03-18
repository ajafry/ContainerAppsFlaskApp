# define variables for cleaner code
$RG_NAME = ''                   # Resource Group Name
$LOCATION = ''                                  # Location where resources will be deployed
$CONTAINER_APP_NAME = ''                        # Name of the container app
$ACA_ENVIRONMENT_NAME = ''                      # Name of the container app environment
$ACR_NAME = ''                                  # Name of the Azure Container Registry
$ACR_REGISTRY_SERVER = "$ACR_NAME.azurecr.io"   # Registry server URL (combines ACR name with azurecr.io)
$IMAGE_NAME = ''                                # Name of the image, this will be the name of image pushed to the registry
$IMAGE_VERSION = ''                             # What version number to tag the image with
$TAG_LINE = 'A tag line'                        # An arbitrary text string that will be displayed on the Flask app's home page
$FULL_IMAGE_IDENTIFIER = "$ACR_REGISTRY_SERVER/${IMAGE_NAME}:$IMAGE_VERSION"

# Using podman to build and image and tagging it with ACR info
podman build -t $FULL_IMAGE_IDENTIFIER .

# Run the image using podmon to test locally
podman run -d --name myflaskapp -p 5000:5000 -e TAG_LINE=$TAG_LINE $FULL_IMAGE_IDENTIFIER

# cleanup locally running containers
podman stop myflaskapp
podman rm myflaskapp

# Retrieve a token to push an image to the registry using podman
$ACR_TOKEN = $(az acr login --name $ACR_NAME --expose-token --query accessToken --output tsv)
podman login $ACR_REGISTRY_SERVER -u 00000000-0000-0000-0000-000000000000 -p $ACR_TOKEN

# Push the image to ACR
podman push $FULL_IMAGE_IDENTIFIER

# To only update the image  (optional if you wish to update the image in the container app after deploying it initially)
az containerapp update --name $CONTAINER_APP_NAME --resource-group $RG_NAME --image $FULL_IMAGE_IDENTIFIER