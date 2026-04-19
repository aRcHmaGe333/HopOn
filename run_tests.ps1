Write-Output "Installing test requirements..."
python -m pip install -r requirements.txt
Write-Output "Running pytest..."
python -m pytest -q
