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

def load_posts():
    with open('blog_data.json', 'r') as f:
        return json.load(f)

def write_posts(posts):
    with open('blog_data.json', 'w') as f:
        json.dump(posts, f, indent=4)

with open("blog_data.json", "w") as file:
    json.dump(blog_posts, file, indent=4)


@app.route("/")
def hello_world():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    posts = load_posts()
    posts = [post for post in posts if post["id"] != post_id]
    write_posts(posts)
    return redirect(url_for("hello_world"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)
    if post is None:
        return "Post not found", 404
    if request.method == "POST":
        post["author"] = request.form.get("author")
        post["title"] = request.form.get("title")
        post["content"] = request.form.get("content")
        write_posts(posts)
        return redirect(url_for("hello_world"))
    return render_template("update.html", post=post)


@app.route("/like/<int:post_id>")
def like_post(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            post["like"] = post.get("like", 0) + 1
    write_posts(posts)
    return redirect(url_for("hello_world"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        posts = load_posts()
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        new_id = max((post["id"] for post in posts), default=0) + 1
        new_post = {"id": new_id, "author": author, "title": title, "content": content, "like": 0}
        posts.append(new_post)
        write_posts(posts)
        return redirect(url_for("hello_world"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
