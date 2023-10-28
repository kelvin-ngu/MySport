import { Component, Input } from '@angular/core';
import { Postlist } from '../postlist';
import { PostComponent } from '../post/post.component';

@Component({
  selector: 'app-player-voice',
  templateUrl: './player-voice.component.html',
  styleUrls: ['./player-voice.component.css'],
  imports: [PostComponent],
  standalone: true
})
export class PlayerVoiceComponent {
  @Input() postList!: Postlist;  
}
