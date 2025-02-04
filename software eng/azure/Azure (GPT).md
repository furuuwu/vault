# Azure (GPT)

## Create a static website and deploy it to Azure Storage

### Step 1: **Create a Static Website Locally**

* Create a folder for your project, e.g., `my-static-website`.
* Inside the folder, create the following files and folders:

  * `index.html` (your main HTML file)
  * `images/` (a folder to store your images)
  * `styles.css` (optional, for styling)

#### Example `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Static Website</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>Welcome to My Static Website!</h1>
<p>This is a simple static website deployed to Azure.</p>
<img src="images/example-image.jpg" alt="Example Image" width="300">
</body>
</html>
```

#### Example `styles.css` (optional)

```css
body {
font-family: Arial, sans-serif;
text-align: center;
background-color: #f0f0f0;
padding: 20px;
}

h1 {
color: #333;
}
```

* Add some images to the `images/` folder, e.g., `example-image.jpg`.

---

### Step 2: **Set Up Azure Storage Account**

* ***Log in to Azure Portal**:

  * Go to the [Azure Portal](https://portal.azure.com/).
  * Log in with your Azure account.

* **Create a Storage Account**:

  * Click on **Create a resource**.
  * Search for **Storage Account** and click **Create**.
  * Fill in the required details:
    * **Subscription**: Select your subscription.
    * **Resource Group**: Create a new one or use an existing one.
    * **Storage Account Name**: Choose a unique name (e.g., `mystaticwebsite123`).
    * **Region**: Select a region close to you.
    * **Performance**: Standard.
    * **Redundancy**: Locally-redundant storage (LRS) is fine for testing.
  * Click **Review + Create**, then **Create**.

* **Enable Static Website Hosting**:

  * Once the storage account is created, go to the resource.
  * In the left menu, scroll down to **Data management** and click **Static website**.
  * Toggle the **Enabled** button to enable static website hosting.
  * Set the **Index document name** to `index.html`.
  * Optionally, set an **Error document path** (e.g., `404.html`).
  * Click **Save**.

* **Upload Your Website Files**:

* In the **Static website** section, note the **Primary endpoint**. This is the URL of your website.
* Go to **Storage Explorer** (in the left menu) or use the **Azure Storage Explorer** app.
* Navigate to the `$web` container (this is where static website files are stored).
* Upload your `index.html`, `styles.css`, and `images/` folder to the `$web` container.

---

### Step 3: **Access Your Static Website**

1. Once the files are uploaded, go back to the **Static website** section in the Azure Portal.
2. Copy the **Primary endpoint** URL (e.g., `https://mystaticwebsite123.z13.web.core.windows.net`).
3. Open the URL in your browser to see your static website live!

---

### Step 4: **Optional: Automate Deployment**

If you want to automate the deployment process, you can use **Azure CLI** or **GitHub Actions**.

#### Using Azure CLI

1. Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
2. Log in to Azure:

   ```bash
   az login
   ```

3. Upload your files to the `$web` container:

   ```bash
   az storage blob upload-batch \
     --account-name <STORAGE_ACCOUNT_NAME> \
     --source ./my-static-website \
     --destination '$web' \
     --overwrite
   ```

#### Using GitHub Actions

1. Create a `.github/workflows/deploy.yml` file in your project:

   ```yaml
   name: Deploy Static Website to Azure

   on:
     push:
       branches:
         - main

   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Upload to Azure Storage
           uses: azure/CLI@v1
           with:
             inlineScript: |
               az storage blob upload-batch \
                 --account-name <STORAGE_ACCOUNT_NAME> \
                 --source ./ \
                 --destination '$web' \
                 --overwrite
   ```

2. Replace `<STORAGE_ACCOUNT_NAME>` with your storage account name.
3. Push your code to GitHub, and the workflow will automatically deploy your website.

---

### Step 5: **Test Your Website**

* Visit the **Primary endpoint** URL in your browser.
* Verify that your website is live and the images are displayed correctly.
