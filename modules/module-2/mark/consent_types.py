"""Consent types"""

_consent_types = {
    "Leg amputation": {
        "full_description": "The surgical removal of all or part of a leg due to injury, disease, or medical necessity.",
        "intended_benefits": "Relief from pain or disability caused by severe injury, disease, or non-functional limb.",
        "potential_risks": "Risk of surgical complications such as infection, bleeding, and nerve damage. Psychological impact of limb loss.",
    },
    "Heart surgery": {
        "full_description": "A procedure performed on the heart to correct defects, treat ischaemic heart disease, or manage other cardiac conditions.",
        "intended_benefits": "Improvement of heart function, relief of symptoms, prevention of complications, and prolongation of life expectancy.",
        "potential_risks": "Risks include bleeding, infection, heart rhythm disturbances, blood clots, stroke, and anesthesia complications.",
    },
    "Cosmetic surgery": {
        "full_description": "Surgical procedures performed to enhance or alter a person's appearance, often elective and not medically necessary.",
        "intended_benefits": "Improved aesthetic appearance, enhanced self-confidence, and psychological well-being.",
        "potential_risks": "Risks include anesthesia complications, infection, scarring, dissatisfaction with results, and potential need for revision surgery.",
    },
    "Blood transfusion": {
        "full_description": "The process of transferring blood or blood products into one's bloodstream, typically to replace lost blood or treat certain medical conditions.",
        "intended_benefits": "Correction of anemia, restoration of blood volume, improvement of oxygen delivery to tissues, and treatment of bleeding disorders.",
        "potential_risks": "Risks include transfusion reactions, transmission of infections, immune-mediated complications, and fluid overload.",
    },
    "Organ donation": {
        "full_description": "The voluntary act of donating organs or tissues for transplantation into another person's body to improve their health or save their life.",
        "intended_benefits": "Saving or improving the lives of recipients, advancing medical research, and providing comfort to donor families.",
        "potential_risks": "Risks to donors are typically minimal but may include surgical complications, infection, and psychological stress.",
    },
    "Endoscopy": {
        "full_description": "A procedure used to examine the interior of a hollow organ or cavity of the body using an endoscope, a flexible tube with a light and camera attached.",
        "intended_benefits": "Diagnosis of gastrointestinal conditions, visualization of abnormalities, biopsy collection, and therapeutic interventions.",
        "potential_risks": "Risks include perforation, bleeding, infection, adverse reactions to sedation, and complications related to specific procedures.",
    },
    "Lumbar puncture": {
        "full_description": "A medical procedure in which a needle is inserted into the spinal canal in the lower back to collect cerebrospinal fluid for diagnostic purposes or to administer medications.",
        "intended_benefits": "Diagnosis of neurological conditions, relief of intracranial pressure, administration of medications directly into the cerebrospinal fluid.",
        "potential_risks": "Risks include headache, bleeding, infection, nerve damage, and rare but serious complications such as brain herniation.",
    },
    "Cataract surgery": {
        "full_description": "A surgical procedure to remove a clouded lens from the eye and replace it with an artificial lens to restore vision impaired by cataracts.",
        "intended_benefits": "Improvement of visual acuity, restoration of color perception, enhanced quality of life, and independence.",
        "potential_risks": "Risks include infection, bleeding, retinal detachment, secondary cataract formation, and dissatisfaction with visual outcomes.",
    },
    "Electroconvulsive therapy (ECT)": {
        "full_description": "A psychiatric treatment in which electric currents are passed through the brain, intentionally triggering a brief seizure to alleviate symptoms of certain mental illnesses.",
        "intended_benefits": "Reduction of symptoms in severe depression, mania, and certain psychiatric disorders resistant to other treatments.",
        "potential_risks": "Risks include memory loss, confusion, headaches, muscle aches, cardiovascular complications, and rarely, death.",
    },
    "In vitro fertilization (IVF)": {
        "full_description": "A fertility treatment in which eggs are retrieved from a woman's ovaries, fertilized with sperm in a laboratory dish, and then transferred to the uterus to establish a pregnancy.",
        "intended_benefits": "Assistance in achieving pregnancy for couples with infertility due to various factors such as ovulatory disorders, tubal factors, or male infertility.",
        "potential_risks": "Risks include multiple pregnancy, ovarian hyperstimulation syndrome, ectopic pregnancy, and psychological stress.",
    },
}


def consent_keys():
    return list(_consent_types.keys())


def get_full_description(consent_type):
    return _consent_types.get(consent_type, {}).get("full_description", "")


def get_intended_benefits(consent_type):
    return _consent_types.get(consent_type, {}).get("intended_benefits", "")


def get_potential_risks(consent_type):
    return _consent_types.get(consent_type, {}).get("potential_risks", "")
