from app.db.database import SessionLocal
from app.models.clinic import Clinic
from app.models.service import Service
from app.models.clinic_service import ClinicService


def seed():
    db = SessionLocal()
    if db.query(Clinic).first():
        db.close()
        return

    malaria = Service(name="Malaria treatment", category="General")
    anc = Service(name="Antenatal care", category="Maternal")
    tb = Service(name="Tuberculosis treatment", category="General")
    hiv = Service(name="HIV/AIDS counselling", category="General")
    db.add_all([malaria, anc, tb, hiv])
    db.commit()

    connaught = Clinic(
        name="Connaught Hospital",
        district="Western Area Urban",
        clinic_type="Hospital",
        address="Lightfoot Boston St, Freetown",
        latitude=8.487, longitude=-13.234
    )
    bo_clinic = Clinic(
        name="Bo Government Hospital",
        district="Bo",
        clinic_type="Hospital",
        address="Bo, Southern Province",
        latitude=7.964, longitude=-11.738
    )
    makeni = Clinic(
        name="Makeni Regional Hospital",
        district="Bombali",
        clinic_type="Hospital",
        address="Makeni, Northern Province",
        latitude=8.880, longitude=-12.044
    )
    db.add_all([connaught, bo_clinic, makeni])
    db.commit()

    db.add_all([
        ClinicService(clinic_id=connaught.id, service_id=malaria.id, is_free=False, fee=50.0),
        ClinicService(clinic_id=connaught.id, service_id=anc.id, is_free=True),
        ClinicService(clinic_id=bo_clinic.id, service_id=malaria.id, is_free=True),
        ClinicService(clinic_id=bo_clinic.id, service_id=tb.id, is_free=True),
        ClinicService(clinic_id=makeni.id, service_id=hiv.id, is_free=True),
        ClinicService(clinic_id=makeni.id, service_id=anc.id, is_free=True),
    ])
    db.commit()
    db.close()
    print("Demo data seeded successfully")


if __name__ == "__main__":
    seed()
