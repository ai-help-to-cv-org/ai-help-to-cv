# AI-Help-to-CV

AI-Help-to-CV, yapay zeka destekli, kullanıcıların özgeçmiş (CV) hazırlamalarını ve mülakat pratiği yapmalarını kolaylaştıran bir web uygulamasıdır. Proje, modern frontend ve backend teknolojileri ile iki geliştirici tarafından aktif olarak geliştirilmektedir.

## 🚀 Özellikler

- E-posta ve Google ile giriş/kayıt (JWT tabanlı kimlik doğrulama)
- Kullanıcıya özel Dashboard ve günlük görevler
- CV oluşturma ve öneri alma (AI ile)
- Mülakat soruları ve cevapları (AI ile)
- Gamification: Görevler, ilerleme çubuğu, motivasyon mesajları
- API-temelli mimari (React & FastAPI)
- Responsive tasarım (Bootstrap)
- PDF olarak CV indirme
- Veritabanı: PostgreSQL veya MySQL desteği, SQLAlchemy ORM ile

## 🛠️ Kullanılan Teknolojiler

**Frontend**
- React (Vite veya CRA)
- Bootstrap
- Axios

**Backend**
- FastAPI
- SQLAlchemy & Alembic (ORM ve migration)
- JWT Authentication
- PostgreSQL/MySQL

**AI & Diğer**
- OpenAI ChatGPT API (CV ve mülakat için)
- (Gelecekte) LinkedIn/Indeed scraping, Udemy/Coursera API entegrasyonu

## 📂 Proje Yapısı ve Branch Stratejisi

- `main` → Release/Production branch
- `frontend` → Frontend geliştirme (Suat)
- `backend` → Backend geliştirme (Samet)
- Özellik/iş bazlı branchler: `feature/issue-xx-özellik-ismi`, `bugfix/issue-yy-hata-aciklamasi` vb.

## 🚦 İş Akışı & Katkı

1. **Issues** sekmesinden yapılacak işler belirlenir ve atanır.
2. Her iş için ana branchlerden (frontend/backend/main) yeni bir branch açılır.
3. Geliştirme tamamlanınca Pull Request açılır, kod gözden geçirilir ve birleştirilir (merge).
4. Ana branchler sadece PR ile güncellenir.

## 🚧 Yol Haritası (Milestones)

### Milestone 1: MVP Başlangıç
- [x] React & FastAPI setup
- [x] Login/Register, Dashboard, Dummy Data
- [ ] Database şeması ve migration
- [ ] Temel API entegrasyonu

### Milestone 2: CV & Interview
- [ ] CV formu ve AI öneri
- [ ] Mülakat sayfası ve soru-cevap
- [ ] PDF export

### Milestone 3: Gamification & Motivasyon
- [ ] Günlük görevler, ilerleme çubuğu
- [ ] Motivasyon e-mailleri

### Milestone 4: Gelişmiş Özellikler
- [ ] LinkedIn/Indeed scraping
- [ ] Eğitim/kurs önerileri
- [ ] Community/yorum sistemi

## ⚡ Kurulum

### Backend için:
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend için:
```bash
cd frontend
npm install
npm run dev
```

### Veritabanı migrasyonu:
```bash
alembic upgrade head
```

## 🤝 Katkı Sağlamak İçin

- Lütfen önce bir issue açın veya bir issue'ya assign olun.
- PR açarken açıklama ekleyin ve ilgili issue'yu belirtin (örn: Closes #12).
- Kod standartlarına uygun geliştirme yapmaya özen gösterin.

## 📧 İletişim

- **Frontend:** Suat
- **Backend:** Samet

Her türlü soru ve katkı için issue/pull request açabilirsiniz.

> **Not:** Proje aktif geliştirme aşamasındadır. Yapay zeka entegrasyonları ve diğer ileri özellikler ilerleyen milestone'larda eklenecektir.