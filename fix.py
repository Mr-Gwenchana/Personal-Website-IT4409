import sys

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ðang ký nh?n tin - Nguy?n Hi?u</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Caveat:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="main-page">
        <div class="top-controls">
            <a href="index.html" class="nav-btn">Trang ch?</a>
            <div class="theme-switch-wrapper">
                <label class="theme-switch" for="checkbox">
                    <input type="checkbox" id="checkbox" />
                    <div class="slider round">
                        <svg class="sun" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg class="moon" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </div>
                </label>
            </div>
        </div>

        <section class="register-section">
            <div class="register-container">
                <h2 class="section-title" style="margin-bottom: 20px; font-size: 3rem;">Ðang ký nh?n thông tin</h2>
                <p class="register-subtitle">Ð?ng b? l? nh?ng c?p nh?t m?i nh?t t? H?u nhé!</p>
                
                <form class="register-form" action="#" method="POST" id="registerForm">
                    <div class="form-group">
                        <label for="fullname">H? và tên <span style="color: red;">*</span></label>
                        <input type="text" id="fullname" name="fullname" placeholder="Nh?p h? tên c?a b?n" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email <span style="color: red;">*</span></label>
                        <input type="email" id="email" name="email" placeholder="Nh?p d?a ch? email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="phone">S? di?n tho?i</label>
                        <input type="tel" id="phone" name="phone" placeholder="Nh?p s? di?n tho?i">
                    </div>

                    <div class="form-group">
                        <label>Gi?i tính <span style="color: red;">*</span></label>
                        <div class="gender-options">
                            <div class="gender-option">
                                <input type="radio" id="gender-male" name="gender" value="male" required>
                                <label for="gender-male">Nam</label>
                            </div>
                            <div class="gender-option">
                                <input type="radio" id="gender-female" name="gender" value="female" required>
                                <label for="gender-female">N?</label>
                            </div>
                            <div class="gender-option">
                                <input type="radio" id="gender-other" name="gender" value="other" required>
                                <label for="gender-other">Khác</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="interest">Ch? d? quan tâm</label>
                        <select id="interest" name="interest">
                            <option value="tech">Công ngh? & IT</option>
                            <option value="life">Cu?c s?ng d?i thu?ng</option>
                            <option value="f1">Ðua xe F1</option>
                            <option value="music">Âm nh?c</option>
                            <option value="gaming">Trò choi di?n t?</option>
                            <option value="pets">Thú cung</option>
                            <option value="other">Khác</option>
                        </select>
                    </div>

                    <button type="submit" class="submit-btn">Ðang ký ngay</button>
                </form>
            </div>
        </section>
    </div>
    <script src="script.js"></script>
    <script>
        document.getElementById("registerForm").addEventListener("submit", function(e) {
            const fullname = document.getElementById("fullname").value.trim();
            const email = document.getElementById("email").value.trim();
            const gender = document.querySelector("input[name=\"gender\"]:checked");
            
            if (!fullname) {
                alert("Vui lòng nh?p h? và tên!");
                e.preventDefault();
                return;
            }
            if (!email) {
                alert("Vui lòng nh?p email!");
                e.preventDefault();
                return;
            }
            if (!gender) {
                alert("Vui lòng ch?n gi?i tính!");
                e.preventDefault();
                return;
            }
            
            alert("Ðang ký thành công!");
            e.preventDefault(); // for demo
        });
    </script>
</body>
</html>"""

with open("E:/IT4409-Web/register.html", "w", encoding="utf-8") as f:
    f.write(html_content)
