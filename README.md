# django-allauth-boilerplate
boilerplate for django including django allauth with google authentication integrated 

it's still under construction

the boilerplate includes
- black 
- flake8
- python dotenv
- pytest configuration
- django debug toolbar
- ipython for easier terminal experience
- database configuration with postgresql and docker-compose file to have postgresql and redis




if you are using vscode create .vscode directory and add settings.json file 
""" json
{
  "files.watcherExclude": {
    "**/env/**": true,
    "**/node_modules/**": true
  },
  "editor.formatOnSave": true,
  "editor.fontSize": 16,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "95"],
  "python.linting.flake8Args": ["--max-line-length", "95"],
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "[html][django-html][handlebars][hbs][mustache][jinja][jinja-html][nj][njk][nunjucks][twig]": {
    "editor.defaultFormatter": "monosans.djlint",
    "editor.foldingStrategy": "indentation"
  },
  "djlint.formatCss": true,
  "djlint.formatJs": true,
  "djlint.preserveBlankLines": true,
  "djlint.lineBreakAfterMultilineTag": true,
  "python.testing.pytestArgs": ["server"],
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true
}
"""
