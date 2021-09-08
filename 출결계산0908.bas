Attribute VB_Name = "Module21"
Sub count_attendance()
    For i = 1 To 3
        Sheets("출석 및 과제표").Select
        Range("A1").Select
        count_attend_absent = 0
        count_attend_late = 0
        count_homework = 0
        
        For j = 0 To 11
            cell_value = Cells(3 + (i - 1) + (3 * j), 3).Value
            If cell_value = "" Then
                
            ElseIf cell_value = "△" Then
                count_attend_late = count_attend_late + 1
            ElseIf cell_value = "X" Then
                count_attend_absent = count_attend_absent + 1
            End If
            
            cell_value2 = Cells(3 + (i - 1) + (3 * j), 5).Value
            If cell_value2 = "" Then
                Exit For
            End If
            count_homework = count_homework + 5 - cell_value2
            
            
        Next j
        Sheets("벌금합계").Select
        Range("A1").Select
        ActiveCell.Offset(1 + i, 2) = count_attend_absent * 3000
        ActiveCell.Offset(1 + i, 3) = count_attend_late * 2000
        ActiveCell.Offset(1 + i, 4) = count_homework * 1000
    Next i
End Sub
