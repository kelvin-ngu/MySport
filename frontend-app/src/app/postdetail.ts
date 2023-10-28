import { Post } from "./post";

export interface PostDetail {
    comments: Comment[];
    likes: number;
    post: Post;
}
