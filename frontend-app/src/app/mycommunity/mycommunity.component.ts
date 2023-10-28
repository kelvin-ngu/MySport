import { Component, inject, resolveForwardRef } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { PostDetail } from '../postdetail';
import { PostgatheringService } from '../postgathering.service';

@Component({
  selector: 'app-mycommunity',
  templateUrl: './mycommunity.component.html',
  styleUrls: ['./mycommunity.component.css'],
  standalone: true,
  imports: [PostComponent]
})

export class MycommunityComponent {
  postgatheringService: PostgatheringService  = inject(PostgatheringService);
  postDetail!: PostDetail;
  constructor(){
    this.postgatheringService.getPost().subscribe((response) => {
      const jsonString = JSON.stringify(response);
      const jsonObject = JSON.parse(jsonString);
      this.postDetail = jsonObject.post;
      console.log(jsonObject)
    });

  }
}

