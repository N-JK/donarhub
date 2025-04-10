from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
    path('dis/',views.district,name="dist"),
    path('cat/',views.category,name="cat"),
    path('brand/',views.brand,name="brand"),
    path('place/',views.place,name="place"),
    path('deleteplace/<int:pid>',views.deleteplace,name="deleteplace"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('deletesubcategory/<int:sid>',views.deletesubcategory,name="deletesubcategory"),
    path('deletedistrict/<int:did>',views.deletedistrict,name="deletedistrict"),
    path('editdistrict/<int:did>',views.editdistrict,name="editdistrict"),
    path('deletecategory/<int:cid>',views.deletecategory,name="deletecategory"),
    path('editcategory/<int:cid>',views.editcategory,name="editcategory"),
    path('deletebrand/<int:bid>',views.deletebrand,name="deletebrand"),
    path('newlist/',views.newlist,name="newlist"),
    path('rejectedlist/',views.rejectedlist,name="rejectedlist"),
    path('acceptedlist/',views.acceptedlist,name="acceptedlist"),
    path('acceptdonar/<int:aid>',views.acceptdonar,name="acceptdonar"),
    path('rejectdonar/<int:rid>',views.rejectdonar,name="rejectdonar"),
    path('recipientlist/',views.recipientlist,name="recipientlist"),
    path('adminreg/',views.adminreg,name="adminreg"),
    path('editadmin/<int:aid>',views.editadmin,name="editadmin"),
    path('deleteadmin/<int:aid>',views.deleteadmin,name="deleteadmin"),
    path('homepage/',views.homepage,name="homepage"),
    path('payreport/',views.payreport,name="payreport"),
    path('areqreport/',views.areqreport,name="areqreport"),
    path('reqreport/',views.reqreport,name="reqreport"),
    path('complaint/',views.complaint,name="complaint"),
    path('reply/<int:rpid>',views.reply,name="reply"),    
    path('feedback/',views.feedback,name="feedback"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
]
