
### 2. **ایجاد فایل `Jenkinsfile`**

فایل `Jenkinsfile` مراحل پایپ‌لاین Jenkins را برای CI/CD شامل می‌شود. این فایل شامل کلون کردن پروژه، نصب وابستگی‌ها، اجرای تست‌ها و جمع‌آوری فایل‌های استاتیک است.

#### محتوای پیشنهادی برای `Jenkinsfile`:

```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/MehdiEsmaty/my-django-shop.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'python3 manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 manage.py test'
            }
        }

        stage('Collect Static Files') {
            steps {
                sh 'python3 manage.py collectstatic --noinput'
            }
        }

        stage('Deploy') {
            steps {
                // در این مرحله می‌توانید پروژه را به سرور تولید ارسال کنید
                // یا فایل‌های استاتیک و تغییرات را اعمال کنید.
            }
        }
    }
}
