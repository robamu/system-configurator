function Git-Status { git status }
Set-Alias -Name gits -Value Git-Status
function Git-Commit { git commit }
Set-Alias -Name gitc -Value Git-Commit
function Git-Add { git add }
Set-Alias -Name gita -Value Git-Add
function Git-AddAll { git add . }
Set-Alias -Name gitaa -Value Git-AddAll
function Git-Diff { git diff }
Set-Alias -Name gitd -Value Git-Diff
function Git-DiffStaged { git diff --staged }
Set-Alias -Name gitds -Value Git-DiffStaged

function Shortcut-Func { nvim "$PROFILE" }
Set-Alias -Name shortcut -Value Shortcut-Func
function Salias-Func { & $PROFILE }
Set-Alias -Name salias -Value Salias-Func 

# oh-my-posh init pwsh | Invoke-Expression
Invoke-Expression (&starship init powershell)
