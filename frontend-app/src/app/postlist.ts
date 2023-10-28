import { PostDetail } from "./postdetail";
export interface Postlist extends Iterable<PostDetail> {
    postlist: Array<PostDetail>;
}
