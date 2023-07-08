# from datetime import timedelta
# import requests
# from os import environ
# # from database.connect import redis_client
# from fastapi.responses import JSONResponse


# def auth0_login(username, password):
#     data = {
#         "client_id": environ.get("client_id"),
#         "client_secret": environ.get("client_secret"),
#         "username": username,
#         "password": password,
#         "grant_type": "password",
#     }

#     response = requests.post(environ.get("url_token"), data=data)

#     try:
#         access_token = response.json()["access_token"]

#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#         }

#         response = requests.get(environ.get("url"), headers=headers)
#         res = response.json()
#         email = res["email"]

#         redis_client.set(access_token, email)
#         redis_client.expire(access_token, timedelta(seconds=4 * 3600))

#         response = JSONResponse(content={"success": True, "token": access_token})
#         response.set_cookie("Authorization", f"Bearer {access_token}", httponly=True, expires=4 * 3600)
#         response.set_cookie("email", f"{email}", httponly=True, expires=4 * 3600)
#         return response
#     except Exception as e:
#         print(e)
#         return JSONResponse(
#             content={"success": False, "message": "Wrong email or password"},
#             status_code=401,
#         )
