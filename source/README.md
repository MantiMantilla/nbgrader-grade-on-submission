# Deploy bash script as systemd service.

The following steps will allow you to deploy this script as a continuously executing systemd service.

## 1. Add script to VM file system.

From a terminal with access to the nbgrader extensions (jupyter termminal, most likely), run the following commands:

```bash
mkdir ~/autograde_job/
wget "https://raw.githubusercontent.com/MantiMantilla/nbgrader-grade-on-submission/main/source/watch%2C%20collect%2C%20grade%2C%20release.sh" -O ~/autograde_job/grade_on_submit.sh
```

This downloads a shell script to to your `~/autograde_job` directory that, when running, watches for changes to the nbgrader default exchange directory and performs some tasks when it detects a new subdirectory being created.

1. Collects all submissions of the respective assignment.
2. Grades only the new submission, forcing an override on previous grades of the same assignment.
3. Generates html feedback of only the respective submission.
4. Releases the feedback of only the respective student.

## 2. Execute and persist the process.

Run the following commands:

```bash
chmod +x ~/autograde_job/grade_on_submit.sh
nohup ~/autograde_job/grade_on_submit.sh &
```

This executes the script as a background process and writes all logs to a `nohup.out` file. The process will persist after the session ends.

If needed, you can use `ps` and `pkill` to interrupt the process.

The process will not persist on reboot. Also, we chose not to run this as a systemd service because we need accedd to the JupyterHub session and its extensions.

You may press any key to return to the terminal.
