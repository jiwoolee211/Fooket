from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Comment
from .forms import RestaurantForm, CommentForm

def restaurant_list(request):
    all_res = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': all_res})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('restaurant_list') 
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/restaurant_create.html', {'form': form})

# 1. 맛집 상세 페이지
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    comments = restaurant.comments.all()
    # 상세 페이지에서 바로 댓글 작성을 위한 폼 전달
    comment_form = CommentForm() 
    return render(request, 'restaurants/restaurant_detail.html', {
        'restaurant': restaurant,
        'comments': comments,
        'comment_form': comment_form,
    })

# 2. 댓글 작성
def create_comment(request, res_id):
    if request.method == "POST":
        filled_form = CommentForm(request.POST)
        if filled_form.is_valid(): 
            finished_form = filled_form.save(commit=False)
            finished_form.article = get_object_or_404(Restaurant, pk=res_id)
            finished_form.save()
    return redirect('restaurant_detail', pk=res_id)

# 3. 댓글 삭제 (이름을 comment_delete로 변경!)
def comment_delete(request, restaurant_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('restaurant_detail', pk=restaurant_id)

# 4. 댓글 수정 (이름을 comment_update로 변경!)
def comment_update(request, restaurant_id, comment_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == "POST":
        # CommentForm을 사용하거나 직접 필드 수정
        new_text = request.POST.get('comment_text')
        if new_text:
            comment.comment = new_text
            comment.save() 
        return redirect('restaurant_detail', pk=restaurant_id) 
    
    return render(request, 'restaurants/update_comment.html', {
        'comment': comment,
        'restaurant': restaurant
    })

def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    
    return redirect('restaurant_detail', pk=pk)



def restaurant_update(request, pk):
    
    restaurant = get_object_or_404(Restaurant, pk=pk)
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
    
    return render(request, 'restaurants/restaurant_create.html', {'form': form, 'edit_mode': True})


#페이지네이터
from django.core.paginator import Paginator 

def restaurant_list(request):
    all_res = Restaurant.objects.all().order_by('-id') 
    paginator = Paginator(all_res, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': posts})
    