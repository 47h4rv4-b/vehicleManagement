# from database.connect import redis_client
from fastapi.responses import JSONResponse


# def auth0_logout(auth):
#     response = JSONResponse(
#         content={"success": True, "message": "Logged out successfully"}
#     )
#     response.delete_cookie("Authorization")
#     response.delete_cookie("email")
#     redis_client.delete(auth)  # Clear redis
#     return response
