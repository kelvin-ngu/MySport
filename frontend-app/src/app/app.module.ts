import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { RouterModule } from '@angular/router';
import { MygameComponent } from './mygame/mygame.component';
import { NewEntryComponent } from './new-entry/new-entry.component';
import { EntryboxComponent } from './entrybox/entrybox.component';

@NgModule({
  declarations: [
    AppComponent,
    NewEntryComponent,
    EntryboxComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'mygame', component: MygameComponent}
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
