# npm

```shell
# Initialize a new Node.js project and create package.json
npm init
```

The default package.json file looks like this:

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

```shell
# Runs a custom script defined in package.json
npm run <script>

# Runs the start script defined in package.json. By default this is the development server
npm start
npm run start # same thing
```

```shell
# Installs a package locally in the node_modules directory.
npm install <package>
# eg.
nom install express
```

```json
"dependencies": {
  "express": "^4.18.2"
}
```

```shell
npm install <package> --save-dev
# eg.
npm install jest --save-dev
```

```json
"devDependencies": {
  "jest": "^29.0.0"
}
```

```shell
# Installs a package globally (system-wide).
npm install -g <package>

# Installs all dependencies listed in package.json.
npm install

# Removes a package from the project
npm uninstall <package>
```

do this if some dependency isn't installed correctly

```shell
# Install the missing dependency manually
npm install <dependency_name>

# Reinstall all dependencies
rm -rf node_modules package-lock.json
npm install
```
