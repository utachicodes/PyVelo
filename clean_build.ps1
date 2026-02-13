Get-ChildItem -Recurse -Filter *.egg-info | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
if (Test-Path dist) { Remove-Item dist -Recurse -Force -ErrorAction SilentlyContinue }
if (Test-Path build) { Remove-Item build -Recurse -Force -ErrorAction SilentlyContinue }
Write-Host "Cleaned build artifacts."
python -m build
Write-Host "Build complete. Contents of dist:"
Get-ChildItem dist
