from django.shortcuts import render, HttpResponse, redirect
from ..app_one.models import User, UserManager
from .models import Book, Review
from datetime import datetime, date
from time import gmtime, strftime


# Create your views here.
def index(request):
    print("This is index method in app2 views.py")
    if 'user_id' not in request.session:
        return redirect('app1:index')
    else:
        # fetches session user
        this_user = User.objects.get(id=request.session['user_id'])
        # fetches all the books this user has added
        user_books = Book.objects.filter(adds_book=this_user)
        # counts the number of books this user has added
        user_bookcount = user_books.count()
        print("User is:", this_user.name, "User book count is:", user_bookcount)

        # fetches the 3 most recent reviews for display
        latest3_reviews = Review.objects.order_by("-created_at")[:3]

        context = {
            'books': Book.objects.all(),
            'reviews': latest3_reviews,
        }
        return render(request, 'app_two/books.html', context)


def add_book(request):
    print("This is add_book method in app2 views.py")
    if request.method == "POST":
        print("Post")
        this_user = User.objects.get(id=request.session['user_id'])
        print("User is", this_user.name)
        this_title = request.POST['book_title']
        pick_author = request.POST['pick_author']
        if len(pick_author) > 0:
            this_author = pick_author
        else:
            this_author = request.POST['add_author']

        this_review = request.POST['review']
        this_rating = request.POST['rating']
        print(this_title, this_author, this_review, this_rating)

        # create a Book object with ForeignKey
        new_book = Book.objects.create(adds_book=this_user, title=this_title, author=this_author)

        # create a Review object with 2 ForeignKeys
        new_review = Review.objects.create(user_link=this_user, book_link=new_book,  review=this_review, rating=this_rating)

        return redirect('app2:index')

    else:
        return render(request, 'app_two/add_book.html')


def add_review(request, id):# id of Book object
    print("This is add_review method in app2 views.py")
    print("ID is", id)
    this_user = User.objects.get(id=request.session['user_id'])
    print("User is", this_user.name)
    this_book = Book.objects.get(id=id)
    print("Book is:", this_book.title)
    delete_review = "Delete this Review"

    if request.method == "POST":
        print("Post")
        this_review = request.POST['review']
        this_rating = request.POST['rating']

        print("Rating is:", this_rating, "Review is", this_review)

# create a Review object
        new_review = Review.objects.create(user_link=this_user, book_link=this_book, review=this_review, rating=this_rating)

        return redirect('app2:index')

# displaying reviews
    else:
        # filters Review objects linked to the selected book
        reviews_for_book = Review.objects.filter(book_link=this_book)

        for review in reviews_for_book:
            # user who submitted the review
            print("Reviewer name and ID is", review.user_link.name, review.user_link.id)
            user_id = request.session['user_id']
            # book linked to the review
            book_title = review.book_link.title
            book_id = review.book_link.id
            print("Book title and id are:", book_title, book_id)

            # confirms in terminal whether reviewer and session user are the same person
            if review.user_link.id == user_id:
                print("IDs are equal", review.user_link.id, user_id)
            else:
                print("IDs are not equal", review.user_link.id, user_id)

        context = {
            'book': Book.objects.get(id=id),
            'reviews': reviews_for_book,
        }
        return render(request, 'app_two/add_review.html', context)


def users(request, user_id):
    print("This is users method in app2 views.py")
    this_user = User.objects.get(id=user_id)
    print("User is:", this_user, "User ID is:", user_id)

    # fetches all reviews created by this user
    user_reviews = Review.objects.filter(user_link=this_user)

    # fetches user's 3 most recent reviews for display
    latest3_reviews = user_reviews.order_by("-created_at")[:3]
    context = {
        'user': User.objects.get(id=user_id),
        # sends over the latest 3 reviews
        'books_reviewed': latest3_reviews,
        'count': user_reviews.count(),
    }
    return render(request, 'app_two/users.html', context)


def delete_review(request, review_id):
    print("This is delete_review method in app2 views.py")

    this_user = User.objects.get(id=request.session['user_id'])
    this_review = Review.objects.get(id=review_id)
    reviewer = User.objects.get(userlink=this_review)
    print("User is:", this_user.name, "Review is", this_review.review, "Reviewer is:", reviewer.name)

# this section prevents users from deleting reviews they didn't create
# it's obsolete now that the delete link appears only on session user's reviews
    if this_user != reviewer:
        print("Session user is not reviewer; cannot delete review")
        return redirect('app2:index')
    else:
        print("Session user is reviewer")
        review_to_delete = Review.objects.get(id=review_id)
        print("Review to delete is:", review_to_delete.review, "rating is:", review_to_delete.rating, "ID is", review_id)

# deletes a selected review
        review_to_delete.delete()

        # gets id of selected Book object
        id = review_to_delete.book_link.id
        return redirect('app2:add_review', id)
