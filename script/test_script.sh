#!/bin/bash
echo "script start..."

# n = 10000
for k in $( seq 1 20)
do
    ../src/main 1 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 10000 ${k} 
done
# n = 20000
for k in $( seq 1 20)
do
    ../src/main 1 20000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 20000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 20000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 20000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 20000 ${k}
done
# n = 30000
for k in $( seq 1 20)
do
    ../src/main 1 30000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 30000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 30000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 30000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 30000 ${k}
done
# n = 40000
for k in $( seq 1 20)
do
    ../src/main 1 40000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 40000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 40000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 40000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 40000 ${k}
done
# n = 50000
for k in $( seq 1 20) 
do
    ../src/main 1 50000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 50000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 50000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 50000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 50000 ${k}
done

# n = 100
for k in $( seq 1 20)
do
    ../src/main 1 100 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 100 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 100 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 100 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 100 ${k}
done

# n = 1000
for k in $( seq 1 20)
do
    ../src/main 1 1000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 1000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 1000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 1000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 1000 ${k}
done

# n = 10000
for k in $( seq 1 20)
do
    ../src/main 1 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 10000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 10000 ${k}
done

# n = 100000
for k in $( seq 1 20)
do
    ../src/main 1 100000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 100000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 100000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 100000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 100000 ${k}
done

# n = 1000000
for k in $( seq 1 20)
do
    ../src/main 1 1000000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 2 1000000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 3 1000000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 4 1000000 ${k}
done
for k in $( seq 1 20)
do
    ../src/main 5 1000000 ${k}
done

echo "script finished."