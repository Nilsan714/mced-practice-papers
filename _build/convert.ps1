param([string]$ListFile)
# Converts every .docx path listed (one per line, UTF-8) in $ListFile to PDF using installed Microsoft Word.
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
foreach ($f in (Get-Content -LiteralPath $ListFile -Encoding UTF8)) {
  if (-not $f.Trim()) { continue }
  $d = $w.Documents.Open($f, $false, $true)
  $pdf = [IO.Path]::ChangeExtension($f, '.pdf')
  $d.ExportAsFixedFormat($pdf, 17)
  $d.Close($false)
  Write-Output $pdf
}
$w.Quit()
