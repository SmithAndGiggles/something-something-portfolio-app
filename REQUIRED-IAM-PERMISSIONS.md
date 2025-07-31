# Fix for WIF Service Account Permissions

## The Issue:
Your service account needs additional IAM permissions for Cloud Build and impersonation.

## Required IAM Roles for your service account:
# (me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com)

# 1. Service Account Token Creator (for impersonation)
gcloud projects add-iam-policy-binding me2u-prj-app-prod-3aa8 \
    --member="serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"

# 2. Cloud Build Service Account (for running builds)
gcloud projects add-iam-policy-binding me2u-prj-app-prod-3aa8 \
    --member="serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.builder"

# 3. Artifact Registry Writer (for pushing images)
gcloud projects add-iam-policy-binding me2u-prj-app-prod-3aa8 \
    --member="serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.writer"

# 4. Cloud Run Admin (for deployments)
gcloud projects add-iam-policy-binding me2u-prj-app-prod-3aa8 \
    --member="serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com" \
    --role="roles/run.admin"

# 5. Service Account User (for Cloud Run to use service accounts)
gcloud projects add-iam-policy-binding me2u-prj-app-prod-3aa8 \
    --member="serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

## Alternative: If you prefer to use Terraform, add these to your Terraform configuration:

resource "google_project_iam_member" "github_actions_token_creator" {
  project = "me2u-prj-app-prod-3aa8"
  role    = "roles/iam.serviceAccountTokenCreator"
  member  = "serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com"
}

resource "google_project_iam_member" "github_actions_cloudbuild" {
  project = "me2u-prj-app-prod-3aa8"
  role    = "roles/cloudbuild.builds.builder"
  member  = "serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com"
}

resource "google_project_iam_member" "github_actions_artifact_registry" {
  project = "me2u-prj-app-prod-3aa8"
  role    = "roles/artifactregistry.writer"
  member  = "serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com"
}

resource "google_project_iam_member" "github_actions_cloudrun" {
  project = "me2u-prj-app-prod-3aa8"
  role    = "roles/run.admin"
  member  = "serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com"
}

resource "google_project_iam_member" "github_actions_service_account_user" {
  project = "me2u-prj-app-prod-3aa8"
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:me2u-sa-terraform-prod@me2u-prj-app-prod-3aa8.iam.gserviceaccount.com"
}
