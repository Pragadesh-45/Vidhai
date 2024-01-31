from ultralytics import YOLO
import uuid

from fastapi import FastAPI, File, UploadFile

IMAGEDIR = "Images/"

app = FastAPI()


@app.post("/upload")
async def create_upload_file(file : UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    image = f"/Images/{file.filename}"
  
    # Load a pretrained YOLO model (recommended for training)
    model = YOLO('/tomato_best.pt')

    # Evaluate the model's performance on the validation set
    results = model.predict(source = image)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]  # Access class name using model.names
    
    if class_name == "Bacterial_spot":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Small, brown, water soaked, circular spots with yellow halo on leaves.
                Defoliation of older leaves.
                Small, water-soaked spots on green fruit.
                Centre of spots become irregular, light brown with sunken and scabby surface
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Crystal-Blue-Copper-Oxychloride-500/dp/B08KTJHV2N
                1.0 - 2.0 Gm / Liter of water
                https://www.amazon.in/Blitox-Copper-Oxychloride-Rallis-Fungicide/dp/B0C9MP9PLZ
                1.0 - 2.0 Gm / Liter of water
                https://www.amazon.in/Aries-Agro-Plantomycin-100-Plants/dp/B0C6VT54NF
                0.5 gm - 0.75 gm/Liter of water
            '''
        }

    elif class_name == "Early_blight":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Brown spots with concentric rings in a bull's eye pattern with yellow margin.
                Fruit gets infected through calyx or stem attachment.
                Brown concentric rings on fruits.
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/ANTRACOL-500GMS-PROPINEB-CONTACT-FUNGICIDE/dp/B07CXYFM4Q
                1.0 - 2.0 Gm / Liter of water.
                https://www.amazon.in/UPL-Uthane-m-45-Mancozeb-Fungicide/dp/B07K9S3TPF
                1.5 - 2.0 Gm / Liter of water
                https://www.amazon.in/INDOFIL-M-45-Fungicide-500-g/dp/B07M6ZZWPB
                1.5 - 2.0 Gm / Liter of water
            '''
        }

    elif class_name == "Powdery_Mildew":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Irregular, bright yellow blotches with yellow halo appear on leaves.
                Abundant white sporulation in the infected area of leaves
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Syngenta-Amistar-Top-Fungicide-Pack/dp/B09LV3M79G
                1 ml /litre of water
                https://www.amazon.in/Generic-RALLISHEXA-Contaf-Plus-100ml/dp/B0BTVL68CS
                2 ml/ liter of water
                https://www.amazon.in/Kyoto-Azoxystrobin-Tebuconazole-18-3-Fungicide/dp/B0CSJY8XSR/ref=sr_1_1?crid=Z3B28YZZE2JS&keywords=crystal+kyoto+fungicide&qid=1706455411&sprefix=kyoto+crysta%2Caps%2C342&sr=8-1
                 1.33 ml/liter of water
            '''
        }

    elif class_name == "Septoria Leaf Spot":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Small, round to irregular spots with grey centre and dark margin on leaves.
                Spots coalesce and leaves are blighted.
                Complete defoliation.
                Stems and flowers are affected.
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Crystal-Blue-Copper-Oxychloride-500/dp/B08KTJHV2N
                1- 2 Gm / litre of water
                https://www.amazon.in/Blitox-Copper-Oxychloride-Rallis-Fungicide/dp/B0C9MP9PLZ
                1.0 - 2.0 Gm / Liter of water.
                https://www.amazon.in/Aries-Agro-Plantomycin-100-Plants/dp/B0C6VT54NF
                0.5 gm - 0.75 gm /liter of water
            '''
        }

    elif class_name == "Spider Mites":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Spider mites feed on plant sap, causing tiny, light-colored spots or stippling on the upper surface of leaves.
                Infested leaves may turn yellow, starting from the stippled areas, as the mites withdraw nutrients from the plant.
                Spider mites produce fine silk-like webbing, often found on the undersides of leaves, creating a characteristic webbing appearance.
                Severe infestations can lead to leaf curling, wilting, or even premature leaf drop as the mites damage the plant's vascular system.
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Solomon-Insecticide-Aphids-Jassids-Control/dp/B08QDDK99T/ref=sr_1_1_sspa?crid=2L4S8AJCC2EGM&keywords=solomon+insecticide+bayer&qid=1706455891&sprefix=solomon+inse%2Caps%2C301&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
                200 ml/200 ltr water
                https://www.amazon.in/KATYAYANI-Ozil-Spiromesifen-22-9-50ml/dp/B0CLH2N5BG/ref=sr_1_1?crid=344UQK4RASOC4&keywords=spiromesifen+insecticide&qid=1706455767&sprefix=Spiromesifen%2Caps%2C305&sr=8-1
                3ml to 5ml /Litre of water 
                https://www.amazon.in/Pesticide-Fungicide-Miticide-Insecticide-Flowering/dp/B0CN2VTLHK/ref=sr_1_1?crid=2TPX7JODWX76Z&keywords=dicofol+pesticide&qid=1706455974&sprefix=dicofol+pesticide%2Caps%2C233&sr=8-1
                0.1-0.25 ml/ liter of water
            '''
        }

    elif class_name == "leaf_curl_virus":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Severe stunting of plants
                Downward rolling and crinkling of the leaves
                Older leaves become leathery and brittle
                Shortening of internodes
                Appearance of more lateral branches - bushy appearance
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Bayer-Confidor-Insecticide-Whitefly-Jassids/dp/B08QD5DHMR
                0.75 to 1 ml/liter of water
                https://www.amazon.in/Benevia%C2%AE-Insecticide-FMC-180-ml/dp/B0BV32MHM7
                2ml/liter of water
                https://www.amazon.in/Syngenta-Actara-Thiamethoxam-Insect-Repellent/dp/B08X2NLGF8/ref=sr_1_2?crid=1ZA2HLYOX38EK&keywords=actara&qid=1706458466&sprefix=act%2Caps%2C298&sr=8-2
                0.5 gm/litre of water
            '''
        }

    elif class_name == "leaf_mold":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Leaf mold appears as fuzzy grayish patches on the surface of infected tomato leaves.
                Infected areas exhibit yellowing on the upper side of leaves, progressing to brown patches.
                Unlike spider mites, leaf mold doesn't produce webbing on the plant's surface.
                Leaves may emit a musty or earthy odor, especially when humidity is high.
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Indofil-Contact-Fungicides-Active-Ingredient/dp/B07XZBHHHT/ref=sr_1_1?crid=3AIEXB27SPVQ0&keywords=indofil+z78&qid=1706458937&sprefix=indofil+z%2Caps%2C259&sr=8-1
                2.5 grams /liter of water
            '''
        }

    elif class_name == "mosaic_virus":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Light and dark green mottling on leaves
                Wilting of young leaves
                Leaflets distorted and puckered
                Fern leaf symptoms
                Stunted growth
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/32-Ounce-Safer-Brand-Insect-Killing/dp/B000BQL8UY/ref=sr_1_1?crid=3NRRRIHBEMYUU&keywords=Safer+Brand+5118+Insect+Killing+Soap&qid=1706609076&sprefix=safer+brand+5118+insect+killing+soap%2Caps%2C231&sr=8-1 
		        0.1-0.25 ml/ liter of water
                https://www.amazon.in/Alagaezyme-Neem-Oil-EC-Azadirachtin/dp/B0CS6H6Y85/ref=sr_1_1?crid=12L3WD0SWRKZ7&keywords=Bon-Neem+dosage+per+litre&qid=1706609286&sprefix=bon-neem+dosage+per+litre%2Caps%2C222&sr=8-1 
                4-5 ml /liter of water 
            '''
        }

    elif class_name == "target_spot":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Target spot presents as small, dark, and concentric circular lesions on tomato leaves.
                Lesions often have yellow halos surrounding them, creating a distinctive target-like appearance.
                As the disease advances, the centers of the lesions may dry up and die, leaving a shot-hole effect.
                Severe infections can lead to premature yellowing and dropping of infected leaves.
                Target spot thrives in warm and humid conditions, making proper ventilation and moisture management crucial for prevention.
            ''',
            'PRODUCTS':'''
                https://www.amazon.in/Mizu-Chlorothalonil-Product-Mount-45-Mancozeb/dp/B0CHW7XQY1/ref=sr_1_1?crid=1YC2CMXMO3T9N&keywords=chlorothalonil&qid=1706609367&sprefix=chlorothalonil%2Caps%2C247&sr=8-1 
		        1.5 - 2.0 Gm / Liter of water
                https://www.amazon.in/Crystal-Blue-Copper-Oxy-Chloride/dp/B08QMQ1S74/ref=sr_1_2?crid=154CF6F6248AF&keywords=copper+oxychloride&qid=1706609446&sprefix=copper+oxychloride%2Caps%2C304&sr=8-2 
		        1.0 - 2.0 Gm / Liter of water'''
            
        }

    elif class_name == "late_blight":
        return {
            'DISEASE': class_name,
            'SYMPTOMS': '''
                Water-soaked black lesions on leaves and stems
                Lesions expand rapidly and the entire leaf becomes necrotic.
                White sporulation (sporangia and sporangiophores) on leaves.
                Dark brown lesions on fruit
                Soft rot and disintegration of fruits.
            ''',
            'PRODUCTS': '''
                https://www.amazon.in/Mizu-Chlorothalonil-Product-Mount-45-Mancozeb/dp/B0CHW7XQY1/ref=sr_1_1?adgrpid=63815808917&ext_vrnc=hi&gclid=CjwKCAiAk9itBhASEiwA1my_6ysmPYah4bBto1X-W50yGR3yanjlXkLFOrHUu6XqHm_OC0oYTvmQbhoCtpgQAvD_BwE&hvadid=346110648181&hvdev=c&hvlocphy=9148898&hvnetw=g&hvqmt=e&hvrand=11527849665570667137&hvtargid=kwd-303273741546&hydadcr=12700_1932882&keywords=chlorothalonil&qid=1706457855&sr=8-1
                1.5 - 2.0 Gm / Liter of water
                https://www.amazon.in/Syngenta-Abic-Fungicide-Mancozeb-Grams/dp/B07TGC8ZHT
                1-2gm/litre of water 
                https://www.amazon.in/INDOFIL-M-45-FUNGICIDE-PLANTS-500gm/dp/B0C72F7K89/ref=sr_1_3?crid=1LYXJPA16NYYX&keywords=dithane+m45+fungicide&qid=1706458085&sprefix=dithane+%2Caps%2C344&sr=8-3
                2-2.5 gm per liter of water
            '''
        }
