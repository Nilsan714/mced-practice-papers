param([string]$Path)
# Opens a test copy in Excel, recalculates and prints key results (verifies tracker formulas).
$x = New-Object -ComObject Excel.Application
$x.Visible = $false
$x.DisplayAlerts = $false
$wb = $x.Workbooks.Open($Path)
$x.CalculateFull()
$a = $wb.Worksheets.Item('Attempts')
foreach ($r in 2..4) {
  "Attempts r$r : " + (($a.Range("A$r").Text, $a.Range("D$r").Text, $a.Range("F$r").Text, $a.Range("G$r").Text, $a.Range("H$r").Text, $a.Range("I$r").Text, $a.Range("J$r").Text, $a.Range("K$r").Text, $a.Range("L$r").Text) -join ' | ')
}
$t = $wb.Worksheets.Item('Topic_Accuracy')
foreach ($r in 2..4) {
  $o = @()
  foreach ($c in 1..31) { $o += $t.Cells.Item($r, $c).Text }
  "Topic r$r : " + ($o -join ' | ')
}
$e = $wb.Worksheets.Item('Error_Log')
"Error r2 : " + ((1..8 | ForEach-Object { $e.Cells.Item(2, $_).Text }) -join ' | ')
$rt = $wb.Worksheets.Item('Retest')
"Retest r2 : " + ((1..8 | ForEach-Object { $rt.Cells.Item(2, $_).Text }) -join ' | ')
$b = $wb.Worksheets.Item('Baseline_40')
foreach ($r in 5..12) { "Baseline r$r : " + ((7..12 | ForEach-Object { $b.Cells.Item($r, $_).Text }) -join ' | ') }
$errs = 0
foreach ($ws in $wb.Worksheets) { try { $ec = $ws.UsedRange.SpecialCells(-4123, 16); $errs += $ec.Count; "ERRORS in " + $ws.Name + ": " + $ec.Count } catch {} }
"total formula errors: $errs"
$wb.Close($false)
$x.Quit()
