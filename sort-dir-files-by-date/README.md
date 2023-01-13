## Quickly sort all files in a directory by date (recursive)

### Example

#### Before

```
Day.Month.Year

// before
- dir1
  - file1 (created at 01.02.2020)
  - file2 (created at 02.02.2020)
  - file3 (created at 03.03.2020)
- dir2
  - file4 (created at 01.02.2020)
  - file5 (created at 01.02.2020)
  - file6 (created at 01.02.2020)
- dir3
  - file7 (created at 01.02.2021)
  - file8 (created at 01.02.2023)
  - file (created at 01.02.2022)
  
// after
- dir1
  - 02-2020
      - file1 (created at 01.02.2020)
      - file2 (created at 02.02.2020)
  - 03-2020
      - file3 (created at 03.03.2020)
- dir2
  - 02.2020
      - file4 (created at 01.02.2020)
      - file5 (created at 01.02.2020)
      - file6 (created at 01.02.2020)
- dir3
  - 02-2021
      - file7 (created at 01.02.2021)
  - 02-2022
      - file (created at 01.02.2022)
  - 02-2023
      - file8 (created at 01.02.2023)
```