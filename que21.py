# 21.	Find students enrolled in both courses and students enrolled in only one course.

python={"ram","joya","hari","priya","prem"}
java={"manju","satya","prem","rockey","priya"}

both=python.union(java)
one=python.symmetric_difference(java)
print("student rnrolled in both cources :",both)
print("student enrolled in only one course :",one)

