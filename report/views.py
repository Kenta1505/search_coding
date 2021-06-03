# from django.shortcuts import render
# from django.http import HttpResponse
# from app2.forms import ReportForm
# from report.samurai_search import Searching_samurai
# from report.techacademy_search import Searching_ta
# from report.qiita_search import Searching_qiita
# # Create your views here.

# def index(request):
#     if request.method=='POST':
#         context_results={}
#         kensaku_words=str(request.POST['search'])
#         kensaku_pages=int(request.POST['pages'])
#         checkbox_target_sm=request.POST.get("checkbox_sites_sm", None)
#         checkbox_target_ta=request.POST.get("checkbox_sites_ta", None)
#         checkbox_target_qiita=request.POST.get("checkbox_sites_qiita", None)
        
#         if checkbox_target_sm in 'samurai':
#             S=Searching_samurai()
#             s_results=S.samurai_search(kensaku_words, kensaku_pages)
#             context_samurai={
#                 'titles_sm':s_results[0],
#                 'links_sm':s_results[1]
#             }
#             context_results.update(context_samurai)
#         else:
#             pass
        
#         if checkbox_target_ta in 'ta':
#             T=Searching_ta()
#             t_results=T.ta_search(kensaku_words, kensaku_pages)
#             context_ta={
#                 'titles_ta':t_results[0],
#                 'links_ta':t_results[1],
#                 'setsumei_ta':t_results[2]
#             }
#             context_results.update(context_ta)
#         else:
#             pass
        
#         if checkbox_target_qiita in 'qiita':
#             Q=Searching_qiita()
#             q_results=Q.qiita_search(kensaku_words, kensaku_pages)
#             context_qiita={
#                 'titles_qiita':q_results[0],
#                 'links_qiita':q_results[1],
#                 'setsumei_qiita':q_results[2]
#             }
#             context_results.update(context_qiita)
#         else:
#             pass
        
#         context=(context_results)
#         return render(request, 'top.html', context)

#     else:
#         f=ReportForm({
#             'title':'レポートタイトル',
#             'body':'Hello. Django! Form',
#             }
#         )
#         return render(request, 'top.html', {'form1':f})

