# The Architect 2099 - دليل النشر

## الخطوات اللازمة للنشر على Vercel

### 1. إعداد قاعدة البيانات السحابية (Neon DB)

1. اذهب إلى https://neon.tech وسجل دخول
2. أنشئ قاعدة بيانات جديدة
3. انسخ رابط الاتصال (Connection String)
4. ضعه في ملف `.env.local`:
   ```
   DATABASE_URL=postgresql://user:password@host.neon.tech/dbname
   DATABASE_ASYNC_URL=postgresql+asyncpg://user:password@host.neon.tech/dbname
   ```

### 2. رفع المشروع على GitHub

```bash
cd the_architect_2099

# Initialize git
git init

# Add all files
git add .

# Create commit
git commit -m "Initial commit - The Architect 2099"

# Add remote (WormChatGpt repo)
git remote add origin https://github.com/smartcalculatortools/WormChatGpt.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. النشر على Vercel

#### الطريقة 1: عبر واجهة Vercel (الأسهل)
1. اذهب إلى https://vercel.com/new
2. اختر "Import Git Repository"
3. اختر مستودع WormChatGpt
4. أضف متغيرات البيئة من `.env.local`:
   - `DATABASE_URL`
   - `DATABASE_ASYNC_URL`
   - `SECRET_KEY`
   - `DEBUG=True`
5. اضغط "Deploy"

#### الطريقة 2: عبر Vercel CLI
```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd the_architect_2099
vercel --prod
```

### 4. إضافة مفاتيح API

بعد الحصول على المفاتيح من `.env.local`:

1. في Vercel Dashboard:
   - Settings → Environment Variables
   - أضف جميع المتغيرات

2. في GitHub:
   - Settings → Secrets and variables → Actions
   - أضف `VERCEL_TOKEN` و `GITHUB_TOKEN`

### 5. التحقق من النشر

بعد النشر، افتح:
- `https://your-app.vercel.app/docs` - API Documentation
- `https://your-app.vercel.app/health` - Health Check

## ملاحظات مهمة

⚠️ **تحذير أمان**: لا تشارك مفاتيح API أبداً في المستودع العام!

### الملفات الحساسة (لا ترفعها أبداً):
- [`.env.local`](.env.local) - يحتوي على مفاتيح سرية
- [`backend/.env`](backend/.env) - إعدادات محلية

### ملفات آمنة للرفع:
- [`vercel.json`](vercel.json) - إعدادات Vercel (بدون مفاتيح)
- [`requirements.txt`](requirements.txt) - المكتبات
- جميع ملفات Python

## الحصول على المساعدة

إذا واجهت مشاكل:
1. تحقق من Vercel Function Logs
2. تأكد من أن DATABASE_URL صحيح
3. تحقق من Environment Variables في Vercel
