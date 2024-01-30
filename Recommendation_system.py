# from flask import Flask, request, jsonify

# app = Flask(__name__)

from ultralytics import YOLO

def recognize_disease(image):
  
    # Load a pretrained YOLO model (recommended for training)
    model = YOLO('/home/siva/Documents/Python_Learning/Vidhai/tomato_best.pt')

    # Evaluate the model's performance on the validation set
    results = model.predict(source = image)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]  # Access class name using model.names
        
    return class_name
    
def disease_symptoms_remedies(disease):
    if disease == "Bacterial_spot":
        print(
            '''
            SYMPTOMS :

            Small, brown, water soaked, circular spots with yellow halo on leaves.
            Defoliation of older leaves.
            Small, water-soaked spots on green fruit .
            Centre of spots become irregular, light brown with sunken and scabby surface.

            PRODUCTS :

            https://www.amazon.in/Crystal-Blue-Copper-Oxychloride-500/dp/B08KTJHV2N
            
            https://www.amazon.in/Blitox-Copper-Oxychloride-Rallis-Fungicide/dp/B0C9MP9PLZ

            https://www.amazon.in/Aries-Agro-Plantomycin-100-Plants/dp/B0C6VT54NF



'''
        )

    if disease == "Early_blight":
        print(
            '''
            SYMPTOMS :

            Brown spots with concentric rings in a bull's eye pattern with yellow margin.
            Fruit gets infected through calyx or stem attachment.
            Brown concentric rings on fruits.   

            PRODUCTS :

            https://www.amazon.in/ANTRACOL-500GMS-PROPINEB-CONTACT-FUNGICIDE/dp/B07CXYFM4Q

            https://www.amazon.in/UPL-Uthane-m-45-Mancozeb-Fungicide/dp/B07K9S3TPF
 
            https://www.amazon.in/INDOFIL-M-45-Fungicide-500-g/dp/B07M6ZZWPB         
'''
        )

    if disease == "Powdery_Mildew":
        print(
            '''
            SYMPTOMS :

            Irregular, bright yellow blotches with yellow halo appear on leaves.
            Abundant white sporulation in the infected area of leaves     

            PRODUCTS :

            https://www.amazon.in/Syngenta-Amistar-Top-Fungicide-Pack/dp/B09LV3M79G

            https://www.amazon.in/Generic-RALLISHEXA-Contaf-Plus-100ml/dp/B0BTVL68CS

            https://www.amazon.in/Kyoto-Azoxystrobin-Tebuconazole-18-3-Fungicide/dp/B0CSJY8XSR/ref=sr_1_1?crid=Z3B28YZZE2JS&keywords=crystal+kyoto+fungicide&qid=1706455411&sprefix=kyoto+crysta%2Caps%2C342&sr=8-1


'''
        )
    
    if disease == "Septoria Leaf Spot":
        print(
            '''
            SYMPTOMS :

            Small, round to irregular spots with grey centre and dark margin on leaves.
            Spots coalesce and leaves are blighted.
            Complete defoliation.
            Stems and flowers are affected.            

            PRODUCTS :

            https://www.amazon.in/Crystal-Blue-Copper-Oxychloride-500/dp/B08KTJHV2N

            https://www.amazon.in/Blitox-Copper-Oxychloride-Rallis-Fungicide/dp/B0C9MP9PLZ

            https://www.amazon.in/Aries-Agro-Plantomycin-100-Plants/dp/B0C6VT54NF

'''
        )

    if disease == "Spider Mites":
        print(
            '''
            SYMPTOMS :

            Spider mites feed on plant sap, causing tiny, light-colored spots or stippling on the upper surface of leaves.
            Infested leaves may turn yellow, starting from the stippled areas, as the mites withdraw nutrients from the plant.
            Spider mites produce fine silk-like webbing, often found on the undersides of leaves, creating a characteristic webbing appearance.
            Severe infestations can lead to leaf curling, wilting, or even premature leaf drop as the mites damage the plant's vascular system.            

            PRODUCTS :

            https://www.amazon.in/KATYAYANI-Ozil-Spiromesifen-22-9-50ml/dp/B0CLH2N5BG/ref=sr_1_1?crid=344UQK4RASOC4&keywords=spiromesifen+insecticide&qid=1706455767&sprefix=Spiromesifen%2Caps%2C305&sr=8-1

            https://www.amazon.in/Solomon-Insecticide-Aphids-Jassids-Control/dp/B08QDDK99T/ref=sr_1_1_sspa?crid=2L4S8AJCC2EGM&keywords=solomon+insecticide+bayer&qid=1706455891&sprefix=solomon+inse%2Caps%2C301&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1

            https://www.amazon.in/Pesticide-Fungicide-Miticide-Insecticide-Flowering/dp/B0CN2VTLHK/ref=sr_1_1?crid=2TPX7JODWX76Z&keywords=dicofol+pesticide&qid=1706455974&sprefix=dicofol+pesticide%2Caps%2C233&sr=8-1

'''
        )
    
    if disease == "leaf_curl_virus":
        print(
            '''
            SYMPTOMS :

            Severe stunting of plants
            Downward rolling and crinkling of the leaves
            Older leaves become leathery and brittle
            Shortening of internodes
            Appearence of more lateral branches - bushy appearance

            PRODUCTS :

            https://www.amazon.in/Bayer-Confidor-Insecticide-Whitefly-Jassids/dp/B08QD5DHMR

            https://www.amazon.in/Benevia%C2%AE-Insecticide-FMC-180-ml/dp/B0BV32MHM7

            https://www.amazon.in/Syngenta-Actara-Thiamethoxam-Insect-Repellent/dp/B08X2NLGF8/ref=sr_1_2?crid=1ZA2HLYOX38EK&keywords=actara&qid=1706458466&sprefix=act%2Caps%2C298&sr=8-2

'''
        )

    if disease == "leaf_mold":
        print(
            '''
            SYMPTOMS :

            Leaf mold appears as fuzzy grayish patches on the surface of infected tomato leaves.
            Infected areas exhibit yellowing on the upper side of leaves, progressing to brown patches.
            Unlike spider mites, leaf mold doesn't produce webbing on the plant's surface.
            Leaves may emit a musty or earthy odor, especially when humidity is high.

            PRODUCTS :

            https://www.amazon.in/Indofil-Contact-Fungicides-Active-Ingredient/dp/B07XZBHHHT/ref=sr_1_1?crid=3AIEXB27SPVQ0&keywords=indofil+z78&qid=1706458937&sprefix=indofil+z%2Caps%2C259&sr=8-1

'''
        )

    if disease == "mosaic_virus":
        print(
            '''
            SYMPTOMS :
            Light and dark green mottling on leaves
            Wilting of young leaves
            Leaflets distorted and puckered
            Fern leaf symptoms
            Stunted growth           
'''
        )
    
    if disease == "target_spot":
        print(
            '''
            SYMPTOMS :
            Target spot presents as small, dark, and concentric circular lesions on tomato leaves.
            Lesions often have yellow halos surrounding them, creating a distinctive target-like appearance.
            As the disease advances, the centers of the lesions may dry up and die, leaving a shot-hole effect.
            Severe infections can lead to premature yellowing and dropping of infected leaves.
            Target spot thrives in warm and humid conditions, making proper ventilation and moisture management crucial for prevention.
'''
        )

    if disease == "late_blight":
        print(
            '''
            SYMPTOMS :
            Water-soaked black lesions on leaves and stems
            Lesions expand rapidly and the entire leaf becomes necrotic.
            White sporulation (sporangia and sporangiophores) on leaves.
            Dark brown lesions on fruit
            Soft rot and disintegration of fruits.

            PRODUCTS :

            https://www.amazon.in/Mizu-Chlorothalonil-Product-Mount-45-Mancozeb/dp/B0CHW7XQY1/ref=sr_1_1?adgrpid=63815808917&ext_vrnc=hi&gclid=CjwKCAiAk9itBhASEiwA1my_6ysmPYah4bBto1X-W50yGR3yanjlXkLFOrHUu6XqHm_OC0oYTvmQbhoCtpgQAvD_BwE&hvadid=346110648181&hvdev=c&hvlocphy=9148898&hvnetw=g&hvqmt=e&hvrand=11527849665570667137&hvtargid=kwd-303273741546&hydadcr=12700_1932882&keywords=chlorothalonil&qid=1706457855&sr=8-1

            https://www.amazon.in/Syngenta-Abic-Fungicide-Mancozeb-Grams/dp/B07TGC8ZHT

            https://www.amazon.in/INDOFIL-M-45-FUNGICIDE-PLANTS-500gm/dp/B0C72F7K89/ref=sr_1_3?crid=1LYXJPA16NYYX&keywords=dithane+m45+fungicide&qid=1706458085&sprefix=dithane+%2Caps%2C344&sr=8-3

'''
        )


image = '/home/siva/Documents/Python_Learning/Vidhai/train/Early_blight/0abc57ec-7f3b-482a-8579-21f3b2fb780b___RS_Erly.B 7609.JPG'
disease = recognize_disease(image)
disease_symptoms_remedies(disease)


