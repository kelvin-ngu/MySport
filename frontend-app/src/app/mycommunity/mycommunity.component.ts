import { Component, inject, resolveForwardRef } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { PostDetail } from '../postdetail';
import { PostgatheringService } from '../postgathering.service';
import { Postlist } from '../postlist';

@Component({
  selector: 'app-mycommunity',
  templateUrl: './mycommunity.component.html',
  styleUrls: ['./mycommunity.component.css'],
  standalone: true,
  imports: [PostComponent]
})

export class MycommunityComponent {
  postgatheringService: PostgatheringService  = inject(PostgatheringService);
  postList!: Postlist;
  constructor(){
    this.postgatheringService.getPost().subscribe((response) => {
      const jsonString = JSON.stringify(response);
      this.postList = JSON.parse(jsonString);
      console.log(this.postList);
    });

  }
}

