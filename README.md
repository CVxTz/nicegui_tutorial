# nicegui_tutorial


## Build

```bash
docker build . -t nicegui_app:0.0.1
```

## Run

```bash
docker run -it -p 5000:5000 nicegui_app:0.0.1
```

## Deploy

```bash
PROJECT_ID=$(gcloud config get-value project)
REPO="demo"
LOCATION="europe-west1"
IMAGE="nicegui_app"
SERVICE_NAME="nicegui-app"
VERSION="0.0.1"
GAR_TAG=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE:$VERSION

# Create repository
gcloud artifacts repositories create $REPO --repository-format=docker \
    --location=$LOCATION --description="Docker repository" \
    --project=$PROJECT_ID  || true # If fails because already exist then its fine

# Build image
gcloud builds submit --tag $GAR_TAG

# Deploy Cloud run
gcloud run deploy $SERVICE_NAME --image=$GAR_TAG --max-instances=1 --min-instances=0 --port=8080 \
	--allow-unauthenticated --region=europe-west1 --memory=0.5Gi --cpu=0.5 -q

# Deploy App Engine
## gcloud app deploy --image-url=$GAR_TAG --appyaml=app.yaml
```