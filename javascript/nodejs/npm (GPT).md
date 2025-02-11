# npm (GPT)

## QUESTION: overview of npm

### **A Detailed Overview of NPM (Node Package Manager)**

#### **1. Introduction to NPM**

NPM (Node Package Manager) is the default package manager for **Node.js**. It is a tool that helps developers **install, manage, and share** JavaScript packages (also known as modules). NPM is widely used in the JavaScript ecosystem to manage project dependencies efficiently.

#### **2. Key Features of NPM**

- **Package Management**: Install, update, and remove JavaScript packages with ease.
- **Dependency Management**: Automatically handles dependencies for Node.js applications.
- **Script Running**: Provides a way to run custom scripts (e.g., start a server, run tests, lint code).
- **Registry Access**: Connects to the online **NPM registry** (<https://www.npmjs.com/>) where thousands of open-source packages are available.
- **Version Control**: Supports semantic versioning (`semver`) to maintain package compatibility.
- **Workspace Support**: Enables managing multiple packages within a single project.

---

### **3. NPM Components**

NPM consists of three main parts:

#### **a) NPM CLI (Command Line Interface)**

The **NPM CLI** allows developers to interact with the package manager from the terminal.

#### **b) NPM Registry**

The **NPM registry** is a publicly available online repository where JavaScript developers publish and download packages.

#### **c) NPM Website**

The website **(<https://www.npmjs.com/>)** allows users to browse, search, and explore available packages.

---

### **4. Installing NPM**

NPM comes bundled with **Node.js**, so installing Node.js also installs NPM.

#### **Installation Steps**

1. Download **Node.js** from [Node.js official site](https://nodejs.org/).
2. Install the downloaded package.
3. Verify installation by running:

   ```sh
   node -v  # Checks Node.js version
   npm -v   # Checks NPM version
   ```

---

### **5. Basic NPM Commands**

| Command | Description |
|---------|-------------|
| `npm init` | Initializes a new Node.js project and creates `package.json`. |
| `npm init -y` | Skips prompts and creates `package.json` with default values. |
| `npm install <package>` | Installs a package locally in the `node_modules` directory. |
| `npm install -g <package>` | Installs a package globally (system-wide). |
| `npm install` | Installs all dependencies listed in `package.json`. |
| `npm update` | Updates all installed dependencies to their latest versions. |
| `npm uninstall <package>` | Removes a package from the project. |
| `npm list` | Lists installed packages in the project. |
| `npm outdated` | Checks for outdated packages. |
| `npm audit` | Scans for security vulnerabilities in dependencies. |
| `npm start` | Runs the start script defined in `package.json`. |
| `npm run <script>` | Runs a custom script defined in `package.json`. |

---

### **6. Understanding `package.json` and `package-lock.json`**

#### **a) `package.json`**

- A configuration file that defines project metadata and dependencies.
- Created using `npm init`.
- Example:

  ```json
  {
    "name": "my-project",
    "version": "1.0.0",
    "description": "A sample project",
    "dependencies": {
      "express": "^4.18.2"
    },
    "scripts": {
      "start": "node index.js"
    }
  }
  ```

#### **b) `package-lock.json`**

- Ensures consistent dependency versions across installations.
- Stores the exact versions of installed packages.

---

### **7. Dependency Management in NPM**

NPM supports three types of dependencies:

#### **a) Regular Dependencies (`dependencies`)**

- Installed using `npm install <package>`.
- Example:

  ```json
  "dependencies": {
    "express": "^4.18.2"
  }
  ```

#### **b) Development Dependencies (`devDependencies`)**

- Used only during development (e.g., testing, linting).
- Installed using `npm install <package> --save-dev`.
- Example:

  ```json
  "devDependencies": {
    "jest": "^29.0.0"
  }
  ```

#### **c) Peer Dependencies (`peerDependencies`)**

- Defines compatible versions of dependencies expected in projects.
- Example:

  ```json
  "peerDependencies": {
    "react": "^18.0.0"
  }
  ```

---

### **8. Semantic Versioning (`semver`)**

NPM follows **Semantic Versioning (semver)** for package versioning.

Format: `MAJOR.MINOR.PATCH`

- `1.0.0` → **Major**: Breaking changes.
- `1.1.0` → **Minor**: New features, no breaking changes.
- `1.1.1` → **Patch**: Bug fixes.

Symbols used in `package.json`:

- `^1.2.3` → Allows updates for **minor** and **patch** versions.
- `~1.2.3` → Allows updates for **patch** versions only.

---

### **9. Global vs. Local Installation**

- **Local Installation (default)**: Packages are installed in `node_modules` and listed in `package.json`.

  ```sh
  npm install express
  ```

- **Global Installation**: Packages are installed globally and accessible system-wide.

  ```sh
  npm install -g nodemon
  ```

---

### **10. NPM Scripts**

NPM allows defining scripts in `package.json`:

Example:

```json
"scripts": {
  "start": "node index.js",
  "test": "jest"
}
```

Run scripts using:

```sh
npm run start
npm run test
```

---

### **11. NPM Workspaces**

NPM Workspaces allow managing multiple packages in a single repository.

Example `package.json`:

```json
{
  "workspaces": ["packages/*"]
}
```

Command to install dependencies for all workspaces:

```sh
npm install
```

---

### **12. NPM Audit (Security Scanning)**

NPM provides security checks for vulnerabilities.

- Run security scan:

  ```sh
  npm audit
  ```

- Fix issues automatically:

  ```sh
  npm audit fix
  ```

---

### **13. Publishing a Package on NPM**

#### **Steps to Publish a Package**

1. **Create an NPM account**: [Sign up](https://www.npmjs.com/signup).
2. **Login to NPM**:

   ```sh
   npm login
   ```

3. **Initialize the package**:

   ```sh
   npm init
   ```

4. **Publish the package**:

   ```sh
   npm publish
   ```

5. **Update a package**:

   ```sh
   npm version patch
   npm publish
   ```

---

### **14. Alternative Package Managers**

Other tools built on top of NPM:

- **Yarn**: Faster package manager alternative.
- **pnpm**: Efficient package manager using symlinked modules.
- **Bun**: A modern alternative with built-in performance improvements.
