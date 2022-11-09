# coffee

Sample REST API developed with Python and Flask.

Forked from https://github.com/shawnharris63/coffee.


## A note on Python

You may decide to prefix occurrences of `pip` with `pythonX.X -m pip` where `X.X` represents the explicit version of Python installed on your workstation.

## Clean pip

```bash
pip freeze | xargs pip uninstall -y
```
> See https://stackoverflow.com/questions/11248073/what-is-the-easiest-way-to-remove-all-packages-installed-by-pip.



## Build

If you wish to fork the original Git repository easily, use

```bash
gh repo fork shawnharris63/coffee
```

To prepare `requirements.txt` look in .py files for all `from` and `import` statements

Install dependencies

```
pip install flask
pip install connexion
pip install gunicorn
```
> Make a note of the versions


Now add `requirements.txt`

```
pip freeze > requirements.txt
```

Add `Procfile` to have `gunicorn` serve requests

```bash
cat << EOF >>Procfile
web: gunicorn app:app
EOF
```


## Commit

```
git add .
git commit -m"Add requirements.txt"
git push
```

## Deploy

We're going to target Tanzu Application Platform.

Assume "developer namespace" for workloads was set up as `development`.

HTTPS

```bash
tanzu apps workload create coffee \
  --git-repo https://github.com/pacphi/coffee \
  --git-branch main \
  --type web \
  --namespace development \
  --label app.kubernetes.io/part-of=crypto-screener \
  --annotation autoscaling.knative.dev/minScale=1 \
  --tail
  --yes
```

or

SSH

```bash
tanzu apps workload create coffee \
  --git-repo ssh://git@github.com/pacphi/coffee \
  --git-branch main \
  --type web \
  --namespace development \
  --label app.kubernetes.io/part-of=crypto-screener \
  --annotation autoscaling.knative.dev/minScale=1 \
  --tail
  --yes
```

### Tail logs

```bash
tanzu apps workload tail coffee \
  --namespace development
```

### Diagnostics

```bash
tanzu apps workload get coffee \
  --namespace development
```

## Teardown

```bash
tanzu apps workload delete coffee \
  --namespace development
```
