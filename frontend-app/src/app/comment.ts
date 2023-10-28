import { Player } from "./player";
import { PostDetail } from "./postdetail";

export interface Comment {
    id: number;
    comment: string;
    post: PostDetail;
    author: Player;
    created_at: Date;
}

