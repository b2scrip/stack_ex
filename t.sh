grep -v  "ClosedDate =" a.xml |grep -v "FavoriteCount" |grep -v "AcceptedAnswerId" >> 1
grep "ClosedDate =" a.xml |grep -v "FavoriteCount" |grep -v "AcceptedAnswerId" >> 2
grep -v  "ClosedDate =" a.xml |grep "FavoriteCount" |grep -v "AcceptedAnswerId" >> 3
grep -v  "ClosedDate =" a.xml |grep  -v "FavoriteCount" |grep "AcceptedAnswerId"  >> 4
grep -v  "ClosedDate =" a.xml |grep   "FavoriteCount" |grep "AcceptedAnswerId" >> 5
grep   "ClosedDate =" a.xml |grep  -v "FavoriteCount" |grep "AcceptedAnswerId"  >> 6
grep   "ClosedDate =" a.xml |grep   "FavoriteCount" |grep -v "AcceptedAnswerId" >> 7
grep   "ClosedDate =" a.xml |grep  "FavoriteCount" |grep  "AcceptedAnswerId"  >> 8
