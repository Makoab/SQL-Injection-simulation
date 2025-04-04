# SQLite və Tkinter ilə Sadə Giriş Ekranı

Bu layihə **SQLite** və **Tkinter** istifadə edərək sadə bir giriş ekranı tətbiqini göstərir. Layihə **SQL Injection-a açıq** bir giriş yoxlama metodu ehtiva edir və təhlükəsizlik problemlərini öyrənmək üçün nəzərdə tutulmuşdur.

## Xüsusiyyətlər
- **SQLite verilənlər bazası:** Müvəqqəti yaddaşda (`:memory:`) yaradılan verilənlər bazası.
- **İstifadəçi girişi:** Sadə giriş forması (İstifadəçi adı və şifrə).
- **SQL Injection problemi:** `insecure_login` funksiyası SQL Injection hücumlarına qarşı zəifdir.
- **Tkinter qrafik interfeysi:** İstifadəçi dostu interfeys.

## Quraşdırma və İstifadə

1. **Python 3**-ün sisteminizdə quraşdırıldığından əmin olun.
2. Lazımi kitabxanaları yükləyin (standart Python kitabxanalarıdır, əlavə paket tələb olunmur).
3. **Kod faylını işə salın:**

```sh
python main.py
```

4. Açılan pəncərədə istifadəçi adı və şifrəni daxil edin.
   
   - **admin / admin123**
   - **user / user123**

## Kod Strukturu

- **Verilənlər bazası:** `:memory:` bazasında `users` cədvəli yaradılır.
- **Giriş yoxlaması:** `insecure_login` funksiyası istifadəçi adını və şifrəni birbaşa SQL sorğusuna daxil edir.
- **Qrafik interfeys:** `Tkinter` kitabxanası ilə hazırlanmış sadə giriş ekranı.
- **Girişin yoxlanması:** Daxil edilən məlumatlar `messagebox` vasitəsilə göstərilir.

## Təhlükəsizlik Problemi (SQL Injection)

Bu kodda `insecure_login` funksiyası istifadəçi giriş məlumatlarını birbaşa SQL sorğusuna əlavə edir:

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

Bu metod **SQL Injection** hücumlarına qarşı zəifdir. Məsələn, aşağıdakı kimi giriş edilərsə:

**İstifadəçi adı:** `admin' --`
**Şifrə:** _(boş qala bilər)_

O zaman SQL sorğusu belə olacaq:

```sql
SELECT * FROM users WHERE username='admin' --' AND password=''
```

Bu sorğu `--` şərh işarəsi vasitəsilə şifrə yoxlamasını keçərək `admin` istifadəçisi kimi giriş etməyə imkan verəcək.

## Təhlükəsizlik Təkmilləşdirmələri

Tətbiqdə SQL Injection problemini aradan qaldırmaq üçün `parameterized queries` istifadə etmək tövsiyə olunur:

```python
def secure_login(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    return cursor.fetchone()
```

## Lisensiya
Bu layihə **öyrənmə məqsədi** ilə hazırlanmışdır və açıq mənbəlidir.

---
**Qeyd:** Bu kod **təhlükəsizlik problemləri ilə bağlı maarifləndirmə məqsədi** daşıyır və real sistemlərdə istifadə üçün uyğun deyil!

