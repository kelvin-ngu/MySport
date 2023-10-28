import { Component, inject } from '@angular/core';
import { PostentryService } from '../postentry.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-entrybox',
  templateUrl: './entrybox.component.html',
  styleUrls: ['./entrybox.component.css'],
  imports: [CommonModule],
  standalone: true
})
export class EntryboxComponent {
  postEntryService: PostentryService = inject(PostentryService);
  postEntry(title: string, get_up: string, feelings:string, entry: string, restriction:string) {
    const jsonEntry = <JSON><unknown>{
      player: "c0b4902b-4007-4cfc-838c-07fa4820cc15",
      public: restriction,
      title: title,
      get_up: get_up,
      feelings: feelings,
      entry: entry
    }
    this.postEntryService.postEntry(jsonEntry).subscribe((response) => {
      console.log(response);
    })
  }
}
