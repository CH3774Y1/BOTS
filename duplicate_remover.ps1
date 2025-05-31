//duplicateremoverbyrahulrachari
$hashes = @{}

# Get all files in the current directory and subdirectories
Get-ChildItem -File -Recurse | ForEach-Object {
    $file = $_.FullName
    $hash = (Get-FileHash $file -Algorithm SHA256).Hash

    if ($hashes[$hash]) {
        Write-Host "Deleting duplicate: $file"
        Remove-Item $file -Force
    } else {
        $hashes[$hash] = $file
    }
}

Write-Host "Duplicate file removal completed!"
