from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.database import SessionLocal
from app.database import DealerproductPG
import csv
import pandas as pd
from io import StringIO
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = FastAPI()


@app.post('/upload/')
async def upload_csv(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        try:
            content = await file.read()
            content = content.decode('utf-8')

            csv_data = pd.read_csv(StringIO(content), delimiter=';',
                                   header=None)
            db = SessionLocal()
            try:
                csv_data = csv_data.iloc[1:]
                for row in csv_data.itertuples(index=False, name=None):
                    if len(row) != 7:
                        continue
                    try:
                        id_val = int(row[0])
                        product_key_val = row[1]
                        price_val = float(row[2])
                        product_url_val = row[3]
                        product_name_val = row[4]
                        date_val = row[5]
                        dealer_id_val = int(row[6])
                    except (ValueError, IndexError):
                        logger.error(f'Ошибка в строке: {row}', exc_info=True)
                        continue
            # csv_reader = csv.reader(StringIO(content), delimiter=';')
            # db = SessionLocal()
            # try:
            #     next(csv_reader)
            #     for row in csv_reader:
            #         # if len(row) != 7:
            #         #     continue
            #         try:
            #             id_val = int(row[0])
            #             product_key_val = row[1]
            #             price_val = float(row[2])
            #             product_url_val = row[3]
            #             product_name_val = row[4]
            #             date_val = row[5]
            #             dealer_id_val = int(row[6])
            #         except (ValueError, IndexError):
            #             continue
                    existing_product = db.query(DealerproductPG).filter_by(
                        product_key=product_key_val,
                        dealer_id=dealer_id_val
                    ).first()
                    if existing_product:
                        if existing_product.id != id_val:
                            existing_product.id = id_val
                        if existing_product.price != price_val:
                            existing_product.price = price_val
                        if existing_product.product_url != product_url_val:
                            existing_product.product_url = product_url_val
                        if existing_product.product_name != product_name_val:
                            existing_product.product_name = product_name_val
                        if existing_product.product_name != date_val:
                            existing_product.product_name = date_val
                    else:
                        new_product = DealerproductPG(
                            id=id_val,
                            product_key=product_key_val,
                            price=price_val,
                            product_url=product_url_val,
                            product_name=product_name_val,
                            date=date_val,
                            dealer_id=dealer_id_val
                        )
                        db.add(new_product)
                db.commit()
                return {'message': 'Файл успешно загружен и данные сохранены'}
            except Exception as e:
                db.rollback()
                return JSONResponse(status_code=500, content={"message": str(e)})
            finally:
                db.close()
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})
    else:
        return {'error': 'Неверный формат файла. Пожалуйста загрузите CSV файл'}


@app.get('/')
async def get_products():
    db = SessionLocal()
    try:
        products = db.query(DealerproductPG).all()
        return products
    except Exception as e:
        return {'error': str(e)}
    finally:
        db.close()
