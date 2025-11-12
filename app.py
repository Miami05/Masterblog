import json

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


blog_posts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is my first post.",
        "like": 0,
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is another post.",
        "like": 0,
    },
]

with open("blog_data.json", "w") as file:
    json.dump(blog_posts, file, indent=4)


@app.route("/")
def hello_world():
    return render_template("index.html", posts=blog_posts)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    with open("blog_data.json", "w") as file:
        json.dump(blog_posts, file, indent=4)
    return redirect(url_for("hello_world"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    global blog_posts
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if post is None:
        return "Post not found", 404
    if request.method == "POST":
        post["author"] = request.form.get("author")
        post["title"] = request.form.get("title")
        post["content"] = request.form.get("content")
        with open("blog_data.json", "w") as file:
            json.dump(blog_posts, file, indent=4)
        return redirect(url_for("hello_world"))
    return render_template("update.html", post=post)


@app.route("/like/<int:post_id>")
def like_post(post_id):
    global blog_posts
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if post:
        post["like"] += 1
        with open("blog_data.json", "w") as file:
            json.dump(blog_posts, file, indent=4)
    return redirect(url_for("hello_world"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        new_id = max(post["id"] for post in blog_posts) + 1 if blog_posts else 1

        new_post = {"id": new_id, "author": author, "title": title, "content": content}
        blog_posts.append(new_post)
        with open("blog_data.json", "w") as file:
            json.dump(blog_posts, file, indent=4)
        return redirect(url_for("hello_world"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
