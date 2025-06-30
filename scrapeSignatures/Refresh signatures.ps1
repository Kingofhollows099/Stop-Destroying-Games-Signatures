Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('Your message here')

$excelFilePath = "C:\Users\Geno\OneDrive\Documents\Signatures over time.xlsx"
$excelApp = New-Object -ComObject "Excel.Application"
$excelApp.Visible = $false
$workbook = $excelApp.Workbooks.Open($excelFilePath)
$workbook.RefreshAll()
Start-Sleep -Seconds 30  # Wait for refresh to complete
$workbook.Save()
$workbook.Close()
$excelApp.Quit()
Remove-Variable excelApp, workbook